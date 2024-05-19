from datetime import datetime, timedelta

import httpx
import polars as pl
from dagster import Backoff, RetryPolicy, AssetExecutionContext, asset
from slugify import slugify

from ..resources import AEMETAPI, MITECOArcGisAPI


@asset()
def spain_energy_demand(context: AssetExecutionContext) -> pl.DataFrame:
    """
    Spain energy demand data.
    """
    df = pl.DataFrame()

    ENDPOINT = "https://apidatos.ree.es/en/datos/demanda/demanda-tiempo-real"

    start_date = datetime(2014, 1, 1)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date = start_date + timedelta(days=15)
    end_date_str = end_date.strftime("%Y-%m-%d")

    yesterday = datetime.now() - timedelta(days=1)

    while start_date < yesterday:
        url = f"{ENDPOINT}?start_date={start_date_str}T00:00&end_date={end_date_str}T00:00&time_trunc=hour"
        response = httpx.get(url)

        context.log.info(
            f"Start date: {start_date_str} status code: {response.status_code}"
        )

        local_df = pl.DataFrame(response.json()["included"][0]["attributes"]["values"])
        local_df = local_df.with_columns(
            pl.col("datetime").str.strptime(pl.Datetime, "%Y-%m-%dT%H:%M:%S%.f%z")
        )

        df = pl.concat([df, local_df.select(["value", "datetime"])])

        start_date = start_date + timedelta(days=15)
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date = start_date + timedelta(days=15)
        end_date_str = end_date.strftime("%Y-%m-%d")

    return df


@asset(
    retry_policy=RetryPolicy(max_retries=5, delay=0.2, backoff=Backoff.EXPONENTIAL),
)
def spain_ipc() -> pl.DataFrame:
    """
    Spain IPC data from INE. Downloaded from datos.gob.es (https://datos.gob.es/es/apidata).
    """

    df = pl.read_csv(
        "https://www.ine.es/jaxiT3/files/t/csv_bdsc/50904.csv", separator=";"
    )

    # Clean data
    df = df.with_columns(
        [
            pl.col("Total").str.replace(",", ".").cast(pl.Float64, strict=False),
            pl.col("Periodo")
            .str.replace("M", "-")
            .str.strptime(pl.Date, format="%Y-%m"),
        ]
    )

    df = df.pivot(
        index=["Periodo", "Clases"],
        columns="Tipo de dato",
        values="Total",
        aggregate_function="sum",
    )

    df = df.select(
        [pl.col(col).alias(slugify(col, separator="_")) for col in df.columns]
    )

    return df


@asset()
def spain_aemet_stations_data(aemet_api: AEMETAPI) -> pl.DataFrame:
    """
    Spain AEMET stations data.
    """

    df = pl.DataFrame(aemet_api.get_all_stations())
    df.with_columns(pl.col("indsinop").cast(pl.Int32, strict=False).alias("indsinop"))

    # Clean latitud and longitud
    def convert_to_decimal(coord):
        degrees = int(coord[:-1][:2])
        minutes = int(coord[:-1][2:4])
        seconds = int(coord[:-1][4:])
        decimal = degrees + minutes / 60 + seconds / 3600
        if coord[-1] in ["S", "W"]:
            decimal = -decimal
        return decimal

    df = df.with_columns(
        [
            pl.col("latitud").apply(convert_to_decimal).alias("latitud"),
            pl.col("longitud").apply(convert_to_decimal).alias("longitud"),
        ]
    )

    return df


@asset()
def spain_aemet_weather_data(
    context: AssetExecutionContext, aemet_api: AEMETAPI
) -> pl.DataFrame:
    """
    Spain weather data since 1950.
    """

    start_date = datetime(1950, 3, 1)
    end_date = datetime.now()

    df = pl.DataFrame()

    for i in pl.datetime_range(start_date, end_date, interval="1mo", eager=True):
        pl.col("dates").dt.month_end()

        first_day = i.strftime("%Y-%m-01") + "T00:00:00UTC"
        last_day = (i.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(
            days=1
        )
        last_day = last_day.strftime("%Y-%m-%d") + "T23:59:59UTC"

        context.log.info(f"Getting data from {first_day} to {last_day}")

        mdf = pl.DataFrame(aemet_api.get_weather_data(first_day, last_day))

        df = pl.concat([df, mdf], how="diagonal")

    df = df.with_columns(pl.col("fecha").str.strptime(pl.Date, format="%Y-%m-%d"))

    float_columns = [
        "prec",
        "presMax",
        "presMin",
        "racha",
        "sol",
        "tmax",
        "tmed",
        "tmin",
        "velmedia",
    ]

    df = df.with_columns(
        [
            pl.col(col).str.replace(",", ".").cast(pl.Float64, strict=False)
            for col in float_columns
        ]
    )

    return df


@asset()
def spain_water_reservoirs_data(
    context: AssetExecutionContext, miteco_api: MITECOArcGisAPI
) -> pl.DataFrame:
    """
    Spain water reservoirs data since 1988.

    Data obtained from the ArcGIS server hosted by MITECO (Ministerio para la Transición Ecológica
     y el Reto Demográfico).

    The data are also available on this website:
     https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/boletin-hidrologico.html
    """
    start_year = 1988
    current_year = datetime.now().year

    df = pl.DataFrame()

    for year in range(start_year, current_year + 1):
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        context.log.info(
            f"Getting data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
        )
        response = miteco_api.get_water_reservoirs_data(start_date, end_date)
        if response["features"]:
            mdf = pl.from_records(
                [elem["attributes"] for elem in response["features"]],
                infer_schema_length=None,
            )
            df = pl.concat([df, mdf], how="diagonal_relaxed")

    df = df.with_columns(pl.col("fecha").cast(pl.Datetime("ms")))

    return df

from datetime import datetime

import pandas as pd
import requests
from dagster import Backoff, RetryPolicy, AssetExecutionContext, asset
from slugify import slugify
from pandas.tseries.offsets import MonthEnd

from ..resources import AEMETAPI, MITECOArcGisAPI


@asset()
def spain_energy_demand(context: AssetExecutionContext) -> pd.DataFrame:
    """
    Spain energy demand data.
    """
    df = pd.DataFrame()

    FIRST_DAY = pd.to_datetime("2014-01-01")
    ENDPOINT = "https://apidatos.ree.es/en/datos/demanda/demanda-tiempo-real"

    start_date = pd.to_datetime(FIRST_DAY)
    start_date_str = start_date.strftime("%Y-%m-%d")
    end_date = start_date + pd.DateOffset(days=15)
    end_date_str = end_date.strftime("%Y-%m-%d")

    yesterday = pd.to_datetime("today") - pd.DateOffset(days=1)

    while start_date < yesterday:
        url = f"{ENDPOINT}?start_date={start_date_str}T00:00&end_date={end_date_str}T00:00&time_trunc=hour"
        response = requests.get(url)

        context.log.info(
            f"Start date: {start_date_str} status code: {response.status_code}"
        )

        local_df = pd.json_normalize(
            response.json()["included"][0]["attributes"]["values"]
        )
        local_df["datetime"] = pd.to_datetime(local_df["datetime"], utc=True)

        df = pd.concat([df, local_df[["value", "datetime"]]])

        start_date = start_date + pd.DateOffset(days=15)
        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date = start_date + pd.DateOffset(days=15)
        end_date_str = end_date.strftime("%Y-%m-%d")

    return df


@asset(
    retry_policy=RetryPolicy(max_retries=5, delay=0.2, backoff=Backoff.EXPONENTIAL),
)
def spain_ipc() -> pd.DataFrame:
    """
    Spain IPC data from INE. Downloaded from datos.gob.es (https://datos.gob.es/es/apidata).
    """

    df = pd.read_csv("https://www.ine.es/jaxiT3/files/t/csv_bdsc/50904.csv", sep=";")

    # Clean data
    df["Total"] = pd.to_numeric(df["Total"].str.replace(",", "."), errors="coerce")
    df["Periodo"] = pd.to_datetime(df["Periodo"].str.replace("M", "-"), format="%Y-%m")

    df = df.pivot_table(
        index=["Periodo", "Clases"],
        columns=["Tipo de dato"],
        values="Total",
        aggfunc="sum",
    ).reset_index()

    df.columns = [slugify(col, separator="_") for col in df.columns]

    return df


@asset()
def spain_aemet_stations_data(aemet_api: AEMETAPI) -> pd.DataFrame:
    """
    Spain AEMET stations data.
    """

    df = pd.DataFrame(aemet_api.get_all_stations())

    # Clean latitud and longitud
    df["latitude_sign"] = df["latitud"].str[-1]
    df["longitude_sign"] = df["longitud"].str[-1]

    df["latitud"] = pd.to_numeric(
        df["latitud"].str[:-1].str.replace(",", "."), errors="coerce"
    )
    df["longitud"] = pd.to_numeric(
        df["longitud"].str[:-1].str.replace(",", "."), errors="coerce"
    )

    df["latitud"] = df["latitud"] * df["latitude_sign"].apply(
        lambda x: 1 if x == "N" else -1
    )
    df["longitud"] = df["longitud"] * df["longitude_sign"].apply(
        lambda x: 1 if x == "E" else -1
    )

    df = df.drop(columns=["latitude_sign", "longitude_sign"])

    df = df.convert_dtypes(dtype_backend="pyarrow")

    return df


@asset()
def spain_aemet_weather_data(
    context: AssetExecutionContext, aemet_api: AEMETAPI
) -> pd.DataFrame:
    """
    Spain weather data since 1950.
    """

    start_date = pd.to_datetime("1950-01-01")
    end_date = datetime.now() + MonthEnd(1)

    df = pd.DataFrame()

    for i in pd.date_range(start_date, end_date, freq="M", inclusive="right"):
        first_day = i.strftime("%Y-%m-01") + "T00:00:00UTC"
        last_day = (i + MonthEnd(0)).strftime("%Y-%m-%d") + "T23:59:59UTC"

        context.log.info(f"Getting data from {first_day} to {last_day}")

        mdf = pd.DataFrame(aemet_api.get_weather_data(first_day, last_day))

        df = pd.concat([df, mdf], ignore_index=True)

    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")

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

    df[float_columns] = df[float_columns].apply(lambda x: x.str.replace(",", "."))
    df[float_columns] = df[float_columns].apply(pd.to_numeric, errors="coerce")

    return df


@asset()
def spain_water_reservoirs_data(
    context: AssetExecutionContext, miteco_api: MITECOArcGisAPI
) -> pd.DataFrame:
    """
    Spain water reservoirs data since 1988.

    Data obtained from the ArcGIS server hosted by MITECO (Ministerio para la Transición Ecológica
     y el Reto Demográfico).

    The data are also available on this website:
     https://www.miteco.gob.es/es/agua/temas/evaluacion-de-los-recursos-hidricos/boletin-hidrologico.html
    """
    start_year = 1988
    current_year = datetime.now().year

    df = pd.DataFrame()

    for year in range(start_year, current_year + 1):
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)
        context.log.info(
            f"Getting data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
        )
        response = miteco_api.get_water_reservoirs_data(start_date, end_date)
        if response["features"]:
            mdf = pd.DataFrame.from_dict(
                (elem["attributes"] for elem in response["features"]),  # type: ignore
                orient="columns",
            )
            df = pd.concat([df, mdf], ignore_index=True)

    df["fecha"] = pd.to_datetime(df["fecha"], unit="ms")
    df = df.convert_dtypes(dtype_backend="pyarrow")

    return df

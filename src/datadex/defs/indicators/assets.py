import io
import zipfile

import dagster as dg
import httpx
import polars as pl


@dg.asset
def owid_energy_data() -> pl.DataFrame:
    """
    Raw Energy data from Our World in Data.
    """
    energy_owid_url = (
        "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    )

    return pl.read_csv(
        energy_owid_url, try_parse_dates=True, infer_schema_length=None
    ).shrink_to_fit()


@dg.asset
def owid_co2_data() -> pl.DataFrame:
    """
    Raw CO2 data from Our World in Data.
    """
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )

    return pl.read_csv(co2_owid_url)


@dg.asset(metadata={"publish": ["huggingface"]})
def owid_indicators(
    owid_energy_data: pl.DataFrame, owid_co2_data: pl.DataFrame
) -> pl.DataFrame:
    """
    Joined energy and CO2 data from Our World in Data.
    """

    df: pl.DataFrame = owid_energy_data.join(
        owid_co2_data, on=["iso_code", "year"], how="inner", suffix="_co2"
    )

    return df


@dg.asset(metadata={"publish": ["huggingface"]})
def world_development_indicators() -> pl.DataFrame:
    """
    World Development Indicators (WDI) is the World Bank's premier compilation of cross-country comparable data on development.

    Bulk data download is available at https://datatopics.worldbank.org/world-development-indicators/
    """

    url = "https://databankfiles.worldbank.org/public/ddpext_download/WDI_CSV.zip"

    response = httpx.get(url)

    zipfile.ZipFile(io.BytesIO(response.content)).extractall(path="/tmp/")

    # Load the WDICSV.csv file as a DataFrame
    df = pl.read_csv("/tmp/WDICSV.csv")

    # Reshape the dataframe
    df = df.unpivot(
        index=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        value_name="Indicator Value",
        variable_name="Year",
    )

    df = df.with_columns(pl.col("Year").cast(pl.Int32))

    df = df.rename(
        {
            "Country Name": "country_name",
            "Country Code": "country_code",
            "Indicator Name": "indicator_name",
            "Indicator Code": "indicator_code",
            "Year": "year",
            "Indicator Value": "indicator_value",
        }
    )

    df = df.drop_nulls(subset=["indicator_value"])

    return df

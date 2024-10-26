import io
import zipfile

import dagster as dg
import httpx
import polars as pl


@dg.asset()
def owid_energy_data() -> pl.DataFrame:
    """
    Raw Energy data from Our World in Data.
    """
    energy_owid_url = (
        "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    )

    return pl.read_csv(energy_owid_url)


@dg.asset()
def owid_co2_data() -> pl.DataFrame:
    """
    Raw CO2 data from Our World in Data.
    """
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )

    return pl.read_csv(co2_owid_url)


@dg.asset()
def world_bank_wdi() -> pl.DataFrame:
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

    return df

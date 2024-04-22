import io
import zipfile

import pandas as pd
import polars as pl
import requests
from dagster import asset
from slugify import slugify


@asset(io_manager_key="polars_io_manager")
def owid_energy_data() -> pl.DataFrame:
    """
    Raw Energy data from Our World in Data.
    """
    energy_owid_url = (
        "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    )

    return pl.read_csv(energy_owid_url)


@asset(io_manager_key="polars_io_manager")
def owid_co2_data() -> pl.DataFrame:
    """
    Raw CO2 data from Our World in Data.
    """
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )

    return pl.read_csv(co2_owid_url)


@asset()
def world_bank_wdi() -> pd.DataFrame:
    """
    World Development Indicators (WDI) is the World Bank's premier compilation of cross-country comparable data on development.

    Bulk data download is available at https://datatopics.worldbank.org/world-development-indicators/
    """

    url = "https://databankfiles.worldbank.org/public/ddpext_download/WDI_CSV.zip"

    # Download the zip file
    response = requests.get(url)

    # Read the zip file
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    # Extract the zip file
    zip_file.extractall(path="/tmp/")

    # Load the WDICSV.csv file as a pandas DataFrame
    df = pd.read_csv("/tmp/WDICSV.csv")

    # Reshape the dataframe
    melted_data = pd.melt(
        df,
        id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
        var_name="Year",
        value_name="Indicator Value",
    )

    # Now one column per Indicator Name
    pivoted_data = melted_data.pivot_table(
        index=["Country Name", "Country Code", "Year"],
        columns="Indicator Name",
        values="Indicator Value",
    ).reset_index()

    # Clean column names
    pivoted_data.columns = [slugify(col, separator="_") for col in pivoted_data.columns]

    return pivoted_data

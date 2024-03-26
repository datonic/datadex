import pandas as pd
from dagster import asset


@asset
def owid_energy_data() -> pd.DataFrame:
    """
    Raw Energy data from Our World in Data.
    """
    energy_owid_url = (
        "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"
    )
    return pd.read_csv(energy_owid_url)


@asset
def owid_co2_data() -> pd.DataFrame:
    """
    Raw CO2 data from Our World in Data.
    """
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )
    return pd.read_csv(co2_owid_url)

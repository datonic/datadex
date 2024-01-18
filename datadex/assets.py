import pandas as pd
from dagster import asset
from frictionless import Package


@asset
def threatened_animal_species() -> pd.DataFrame:
    p = Package(
        "https://raw.githubusercontent.com/datonic/threatened-animal-species/main/datapackage.yaml"
    )
    return p.get_resource("threatened-species").to_pandas()  # type: ignore


@asset
def owid_co2_data() -> pd.DataFrame:
    co2_owid_url = (
        "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    )
    return pd.read_csv(co2_owid_url)

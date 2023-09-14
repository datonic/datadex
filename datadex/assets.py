import pandas as pd
from dagster import asset

from frictionless import Package


@asset
def raw_threatened_animal_species() -> pd.DataFrame:
    p = Package(
        "https://raw.githubusercontent.com/datonic/threatened-animal-species/main/datapackage.yaml"
    )
    return p.get_resource("threatened-species").to_pandas()

import pandas as pd
from dagster import AssetIn, asset

from ..resources import HuggingFaceResource


def create_hf_asset(dataset_name: str):
    @asset(
        name="huggingface_" + dataset_name,
        ins={"data": AssetIn(dataset_name)},
        group_name="huggingface",
    )
    def hf_asset(data: pd.DataFrame, hf: HuggingFaceResource) -> None:
        """
        Upload data to HuggingFace.
        """
        hf.upload_dataset(data, dataset_name)

    return hf_asset


datasets = [
    "spain_energy_demand",
    "wikidata_asteroids",
    "threatened_animal_species",
    "country_year_indicators",
    "spain_ipc",
    "spain_aemet_historical_weather",
]

assets = []
for dataset in datasets:
    a = create_hf_asset(dataset)
    assets.append(a)

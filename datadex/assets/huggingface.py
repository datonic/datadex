import pandas as pd
from dagster import asset, AssetIn

from ..resources import HuggingFaceResource


def create_hf_asset(dataset_name: str):
    @asset(name="huggingface_" + dataset_name, ins={"data": AssetIn(dataset_name)})
    def hf_asset(data: pd.DataFrame, hf: HuggingFaceResource) -> None:
        """
        Upload data to HuggingFace.
        """
        hf.upload_dataset(data, dataset_name)

    return hf_asset


datasets = [
    "co2_global_trend",
    "spain_energy_demand",
    "owid_energy_data",
    "owid_co2_data",
    "wikidata_asteroids",
    "threatened_animal_species",
    "climate",
]

assets = []
for dataset in datasets:
    a = create_hf_asset(dataset)
    assets.append(a)

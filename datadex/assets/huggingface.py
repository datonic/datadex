import pandas as pd
from dagster import asset

from ..resources import HuggingFaceResource


@asset()
def hf_co2_data(co2_global_trend: pd.DataFrame, hf: HuggingFaceResource) -> None:
    """
    Upload CO2 data to HuggingFace.
    """
    hf.upload_dataset(co2_global_trend, "co2_global_trend")


@asset()
def hf_spain_energy_demand(
    spain_energy_demand: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload Spain energy demand data to HuggingFace.
    """
    hf.upload_dataset(spain_energy_demand, "spain_energy_demand")


@asset()
def hf_owid_energy_data(
    owid_energy_data: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload Our World in Data energy data to HuggingFace.
    """
    hf.upload_dataset(owid_energy_data, "owid_energy_data")


@asset()
def hf_owid_co2_data(owid_co2_data: pd.DataFrame, hf: HuggingFaceResource) -> None:
    """
    Upload Our World in Data CO2 data to HuggingFace.
    """
    hf.upload_dataset(owid_co2_data, "owid_co2_data")


@asset()
def hf_wikidata_asteroids(
    wikidata_asteroids: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload Wikidata asteroids data to HuggingFace.
    """
    hf.upload_dataset(wikidata_asteroids, "wikidata_asteroids")


@asset()
def hf_threatened_animal_species(
    threatened_animal_species: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload IUCN Red List threatened animal species data to HuggingFace.
    """
    hf.upload_dataset(threatened_animal_species, "threatened_animal_species")

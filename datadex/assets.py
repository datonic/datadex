import io
import os

import pandas as pd
import requests
from dagster import AssetExecutionContext, asset

from .resources import HuggingFaceResource


@asset
def threatened_animal_species(context: AssetExecutionContext) -> pd.DataFrame:
    API_ENDPOINT = "https://apiv3.iucnredlist.org/api/v3"
    TOKEN = os.getenv("IUCNREDLIST_TOKEN")

    page = 1
    all_results = []

    while True:
        r = requests.get(f"{API_ENDPOINT}/species/page/{page}?token={TOKEN}")
        context.log.info(f"Page {page} status code: {r.status_code}")
        if r.status_code != 200 or r.json()["result"] == []:
            break
        results = r.json()["result"]
        all_results.extend(results)
        page += 1

    return pd.DataFrame(all_results).drop(
        columns=["infra_rank", "infra_name", "population", "main_common_name"]
    )


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


@asset
def co2_global_trend() -> pd.DataFrame:
    """
    Trends in Atmospheric Carbon Dioxide from NOAA/ESRL.
    """
    co2_noaa_url = "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_trend_gl.csv"
    return pd.read_csv(co2_noaa_url, skiprows=24)


@asset
def wikidata_asteroids() -> pd.DataFrame:
    """
    Wikidata asteroids data.
    """
    url = "https://query.wikidata.org/sparql"
    query = """
        SELECT
            ?asteroidLabel
            ?discovered
            ?discovererLabel
        WHERE {
            ?asteroid wdt:P31 wd:Q3863;  # Retrieve instances of "asteroid"
                        wdt:P61 ?discoverer; # Retrieve discoverer of the asteroid
                        wdt:P575 ?discovered; # Retrieve discovered date of the asteroid
            SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
        ORDER BY DESC(?discovered)
    """

    response = requests.get(
        url, headers={"Accept": "text/csv"}, params={"query": query}
    )

    return pd.read_csv(io.StringIO(response.content.decode("utf-8")))


@asset
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


@asset(group_name="hf")
def hf_co2_data(co2_global_trend: pd.DataFrame, hf: HuggingFaceResource) -> None:
    """
    Upload CO2 data to HuggingFace.
    """
    hf.upload_dataset(co2_global_trend, "co2_global_trend")


@asset(group_name="hf")
def hf_spain_energy_demand(
    spain_energy_demand: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload Spain energy demand data to HuggingFace.
    """
    hf.upload_dataset(spain_energy_demand, "spain_energy_demand")


@asset(group_name="hf")
def hf_owid_energy_data(
    owid_energy_data: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload Our World in Data energy data to HuggingFace.
    """
    hf.upload_dataset(owid_energy_data, "owid_energy_data")


@asset(group_name="hf")
def hf_owid_co2_data(owid_co2_data: pd.DataFrame, hf: HuggingFaceResource) -> None:
    """
    Upload Our World in Data CO2 data to HuggingFace.
    """
    hf.upload_dataset(owid_co2_data, "owid_co2_data")


@asset(group_name="hf")
def hf_wikidata_asteroids(
    wikidata_asteroids: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload Wikidata asteroids data to HuggingFace.
    """
    hf.upload_dataset(wikidata_asteroids, "wikidata_asteroids")


@asset(group_name="hf")
def hf_threatened_animal_species(
    threatened_animal_species: pd.DataFrame, hf: HuggingFaceResource
) -> None:
    """
    Upload IUCN Red List threatened animal species data to HuggingFace.
    """
    hf.upload_dataset(threatened_animal_species, "threatened_animal_species")

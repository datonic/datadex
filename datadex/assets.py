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
def hf_co2_data(co2_global_trend: pd.DataFrame, hf: HuggingFaceResource) -> None:
    """
    CO2 data from Our World in Data.
    """
    hf.upload_dataset(co2_global_trend, "co2_global_trend")

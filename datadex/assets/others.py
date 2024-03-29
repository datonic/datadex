import io

import pandas as pd
import requests
from dagster import AssetExecutionContext, asset

from ..resources import IUCNRedListAPI


@asset
def threatened_animal_species(iucn_redlist_api: IUCNRedListAPI) -> pd.DataFrame:
    """
    Threatened animal species data from the IUCN Red List API.
    """
    page = 1
    all_results = []

    while True:
        results = iucn_redlist_api.get_species(page)
        if results == []:
            break
        all_results.extend(results)
        page += 1

    return pd.DataFrame(all_results).drop(
        columns=["infra_rank", "infra_name", "population", "main_common_name"]
    )


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

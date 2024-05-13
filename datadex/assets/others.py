import io

import pandas as pd
import requests
from dagster import AssetExecutionContext, asset

from ..resources import IUCNRedListAPI


@asset()
def threatened_animal_species(
    context: AssetExecutionContext, iucn_redlist_api: IUCNRedListAPI
) -> pd.DataFrame:
    """
    Threatened animal species data from the IUCN Red List API.
    """
    page = 1
    all_results = []

    while True:
        context.log.info(f"Fetching page {page}...")
        results = iucn_redlist_api.get_species(page)

        context.log.info(f"Got {len(results)} results.")

        if results == []:
            break
        all_results.extend(results)
        page += 1

    return pd.DataFrame(all_results).drop(
        columns=["infra_rank", "infra_name", "population", "main_common_name"]
    )


@asset()
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

    df = pd.read_csv(io.StringIO(response.content.decode("utf-8")))

    return df

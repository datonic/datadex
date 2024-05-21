import os

from dagster import EnvVar, Definitions, load_assets_from_modules
from dagster_dbt import DbtCliResource, load_assets_from_dbt_project
from dagster_duckdb_polars import DuckDBPolarsIOManager

from .assets import spain, others, indicators, huggingface
from .resources import (
    AEMETAPI,
    IUCNRedListAPI,
    MITECOArcGisAPI,
    HuggingFaceResource,
)

DBT_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../dbt/"
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/database.duckdb")

dbt = DbtCliResource(project_dir=DBT_PROJECT_DIR, profiles_dir=DBT_PROJECT_DIR)

dbt_assets = load_assets_from_dbt_project(DBT_PROJECT_DIR, DBT_PROJECT_DIR)
all_assets = load_assets_from_modules([indicators, huggingface, others, spain])

resources = {
    "hf": HuggingFaceResource(token=EnvVar("HUGGINGFACE_TOKEN")),
    "dbt": dbt,
    "iucn_redlist_api": IUCNRedListAPI(token=EnvVar("IUCN_REDLIST_TOKEN")),
    "aemet_api": AEMETAPI(token=EnvVar("AEMET_API_TOKEN")),
    "miteco_api": MITECOArcGisAPI(),
    "io_manager": DuckDBPolarsIOManager(database=DATABASE_PATH, schema="main"),
}

defs = Definitions(assets=[*dbt_assets, *all_assets], resources=resources)

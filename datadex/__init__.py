import os

from dagster import EnvVar, Definitions, load_assets_from_modules
from dagster_dbt import DbtCliResource
from dagster_duckdb_polars import DuckDBPolarsIOManager

from .assets import dbt, spain, others, indicators, huggingface
from .resources import AEMETAPI, IUCNRedListAPI, MITECOArcGisAPI, DatasetPublisher
from .dbt_project import dbt_project

DATABASE_PATH = os.getenv("DATABASE_PATH", "data/database.duckdb")

all_assets = load_assets_from_modules([indicators, huggingface, others, spain, dbt])

resources = {
    "dbt": DbtCliResource(project_dir=dbt_project),
    "io_manager": DuckDBPolarsIOManager(database=DATABASE_PATH, schema="main"),
    "iucn_redlist_api": IUCNRedListAPI(token=EnvVar("IUCN_REDLIST_TOKEN")),
    "aemet_api": AEMETAPI(token=EnvVar("AEMET_API_TOKEN")),
    "miteco_api": MITECOArcGisAPI(),
    "dp": DatasetPublisher(hf_token=EnvVar("HUGGINGFACE_TOKEN")),
}

defs = Definitions(assets=[*all_assets], resources=resources)

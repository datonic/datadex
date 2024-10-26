import os

import dagster as dg

from dagster_dbt import DbtCliResource
from dagster_duckdb_polars import DuckDBPolarsIOManager

from .assets import dbt, spain, others, indicators, huggingface
from .resources import AEMETAPI, IUCNRedListAPI, MITECOArcGisAPI, DatasetPublisher
from .dbt_project import dbt_project

DATABASE_PATH = os.getenv("DATABASE_PATH", "data/database.duckdb")

all_assets = dg.load_assets_from_modules([indicators, huggingface, others, spain, dbt])

resources = {
    "dbt": DbtCliResource(project_dir=dbt_project),
    "io_manager": DuckDBPolarsIOManager(database=DATABASE_PATH, schema="main"),
    "iucn_redlist_api": IUCNRedListAPI(token=dg.EnvVar("IUCN_REDLIST_TOKEN")),
    "aemet_api": AEMETAPI(token=dg.EnvVar("AEMET_API_TOKEN")),
    "miteco_api": MITECOArcGisAPI(),
    "dp": DatasetPublisher(hf_token=dg.EnvVar("HUGGINGFACE_TOKEN")),
}

defs = dg.Definitions(assets=[*all_assets], resources=resources)

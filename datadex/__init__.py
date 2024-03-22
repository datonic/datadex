import os

from dagster import EnvVar, Definitions, load_assets_from_modules
from dagster_dbt import DbtCliResource, load_assets_from_dbt_project
from dagster_duckdb_pandas import DuckDBPandasIOManager

from .assets import energy, huggingface
from .resources import IUCNRedListAPI, HuggingFaceResource

DBT_PROJECT_DIR = os.path.dirname(os.path.abspath(__file__)) + "/../dbt/"
DATABASE_PATH = os.getenv("DATABASE_PATH", "data/database.duckdb")

dbt = DbtCliResource(project_dir=DBT_PROJECT_DIR, profiles_dir=DBT_PROJECT_DIR)

dbt_assets = load_assets_from_dbt_project(DBT_PROJECT_DIR, DBT_PROJECT_DIR)
all_assets = load_assets_from_modules([energy, huggingface])

resources = {
    "hf": HuggingFaceResource(token=EnvVar("HUGGINGFACE_TOKEN")),
    "dbt": dbt,
    "iucn_redlist_api": IUCNRedListAPI(token=EnvVar("IUCN_REDLIST_TOKEN")),
    "io_manager": DuckDBPandasIOManager(database=DATABASE_PATH, schema="main"),
}

defs = Definitions(assets=[*dbt_assets, *all_assets], resources=resources)

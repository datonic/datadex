from dagster import Definitions

from dagster_dbt import dbt_cli_resource
from dagster_dbt import load_assets_from_dbt_project

DBT_PROJECT_DIR = "dbt/"

dbt_resource = dbt_cli_resource.configured(
    {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROJECT_DIR}
)

dbt_assets = load_assets_from_dbt_project(DBT_PROJECT_DIR, DBT_PROJECT_DIR)

resources = {
    "dbt": dbt_resource,
}

defs = Definitions(assets=[*dbt_assets], resources=resources)

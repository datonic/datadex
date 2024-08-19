from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from ..dbt_project import dbt_project


@dbt_assets(manifest=dbt_project.manifest_path)
def dbt_project_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

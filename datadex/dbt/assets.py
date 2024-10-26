import dagster as dg
from dagster_dbt import DbtCliResource, dbt_assets

from datadex.dbt.resources import dbt_project


@dbt_assets(manifest=dbt_project.manifest_path)
def dbt(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

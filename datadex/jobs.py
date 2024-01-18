from dagster import AssetSelection, define_asset_job, load_assets_from_modules

from . import assets

assets = load_assets_from_modules(modules=[assets])

all_assets_job = define_asset_job(
    name="all_assets_job",
    selection=AssetSelection.all(),
)

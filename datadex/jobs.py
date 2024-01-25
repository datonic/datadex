from dagster import AssetSelection, define_asset_job, load_assets_from_modules

from . import assets

assets = load_assets_from_modules(modules=[assets])

data_assets_job = define_asset_job(
    name="data_assets_job",
    selection=AssetSelection.groups("default"),
)

hf_assets_job = define_asset_job(
    name="hf_assets_job",
    selection=AssetSelection.groups("hf"),
)

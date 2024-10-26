import dagster as dg

from datadex.others import assets

others_assets = dg.load_assets_from_modules([assets])

definitions = dg.Definitions(assets=others_assets)

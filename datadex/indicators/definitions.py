import dagster as dg

from datadex.indicators import assets

indicators_assets = dg.load_assets_from_modules([assets])

definitions = dg.Definitions(assets=indicators_assets)

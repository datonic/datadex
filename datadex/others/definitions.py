import dagster as dg

from datadex.others import assets
from datadex.others.resources import AEMETAPI, IUCNRedListAPI, MITECOArcGisAPI

others_assets = dg.load_assets_from_modules([assets])

definitions = dg.Definitions(
    assets=others_assets,
    resources={
        "iucn_redlist_api": IUCNRedListAPI,
        "aemet_api": AEMETAPI,
        "miteco_api": MITECOArcGisAPI,
    },
)

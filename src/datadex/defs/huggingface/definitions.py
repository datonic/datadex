import dagster as dg

from datadex.defs.huggingface.assets import assets
from datadex.defs.huggingface.resources import HuggingFaceDatasetPublisher

definitions = dg.Definitions(
    assets=assets,
    resources={
        "dp": HuggingFaceDatasetPublisher(hf_token=dg.EnvVar("HUGGINGFACE_TOKEN"))
    },
)

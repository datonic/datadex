import dagster as dg

from datadex.huggingface.assets import assets
from datadex.huggingface.resources import HuggingFaceDatasetPublisher

definitions = dg.Definitions(
    assets=assets,
    resources={
        "dp": HuggingFaceDatasetPublisher(hf_token=dg.EnvVar("HUGGINGFACE_TOKEN"))
    },
)

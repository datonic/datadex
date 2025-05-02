import dagster as dg
import polars as pl

from datadex.defs.huggingface.resources import HuggingFaceDatasetPublisher
from datadex.defs.indicators.definitions import definitions as indicators_definitions


def create_hf_asset(asset_spec: dg.AssetSpec):
    @dg.asset(
        name="huggingface_" + asset_spec.key.to_python_identifier(),
        ins={"data": dg.AssetIn(asset_spec.key.to_python_identifier())},
        metadata={
            "dagster/uri": f"https://huggingface.co/datasets/datonic/{asset_spec.key.to_python_identifier()}"
        },
    )
    def hf_asset(data: pl.DataFrame, dp: HuggingFaceDatasetPublisher) -> None:
        """
        Upload data to HuggingFace.
        """

        readme_content = f"""
---
license: mit
---
# {asset_spec.key.to_python_identifier()}

{asset_spec.description or "No description provided"}

This dataset is produced and published automatically by [Datadex](https://github.com/davidgasquez/datadex),
a fully open-source, serverless, and local-first Data Platform that improves how communities collaborate on Open Data.

## Dataset Details
- **Number of rows:** {data.shape[0]}
- **Number of columns:** {data.shape[1]}
"""

        dp.publish(
            dataset=data,
            dataset_name=asset_spec.key.to_python_identifier(),
            username="datonic",
            readme=readme_content,
            generate_datapackage=True,
        )

    return hf_asset


assets: list[dg.AssetsDefinition] = []
for asset_spec in indicators_definitions.get_all_asset_specs():
    if asset_spec.metadata and "huggingface" in asset_spec.metadata.get("publish", []):
        a = create_hf_asset(asset_spec)
        assets.append(a)

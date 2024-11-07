import dagster as dg
import polars as pl

from datadex.huggingface.resources import HuggingFaceDatasetPublisher


def create_hf_asset(dataset_name: str):
    @dg.asset(
        name="huggingface_" + dataset_name, ins={"data": dg.AssetIn(dataset_name)}
    )
    def hf_asset(data: pl.DataFrame, dp: HuggingFaceDatasetPublisher) -> None:
        """
        Upload data to HuggingFace.
        """

        readme_content = f"""
---
license: mit
---
# {dataset_name}

This dataset is produced and published automatically by [Datadex](https://github.com/davidgasquez/datadex),
a fully open-source, serverless, and local-first Data Platform that improves how communities collaborate on Open Data.

## Dataset Details

- **Number of rows:** {data.shape[0]}
- **Number of columns:** {data.shape[1]}
        """

        dp.publish(
            dataset=data,
            dataset_name=dataset_name,
            username="datonic",
            readme=readme_content,
            generate_datapackage=True,
        )

    return hf_asset


datasets = []

assets = []
for dataset in datasets:
    a = create_hf_asset(dataset)
    assets.append(a)

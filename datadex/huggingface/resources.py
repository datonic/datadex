import os
import tempfile
from typing import Optional

import polars as pl
import yaml
from dagster import ConfigurableResource, InitResourceContext, get_dagster_logger
from huggingface_hub import HfApi
from pydantic import PrivateAttr

log = get_dagster_logger()


class HuggingFaceDatasetPublisher(ConfigurableResource):
    hf_token: str

    _api: HfApi = PrivateAttr()

    def setup_for_execution(self, context: InitResourceContext) -> None:
        self._api = HfApi(token=self.hf_token)

    def publish(
        self,
        dataset: pl.DataFrame,
        dataset_name: str,
        username: str,
        readme: Optional[str] = None,
        generate_datapackage: bool = False,
    ):
        with tempfile.TemporaryDirectory() as temp_dir:
            # Define the file path
            data_dir = os.path.join(temp_dir, "data")
            os.makedirs(data_dir, exist_ok=True)
            file_path = os.path.join(data_dir, f"{dataset_name}.parquet")

            # Write the dataset to a parquet file
            dataset.write_parquet(file_path)

            if readme:
                readme_path = os.path.join(temp_dir, "README.md")
                with open(readme_path, "w") as readme_file:
                    readme_file.write(readme)

            if generate_datapackage:
                datapackage = {
                    "name": dataset_name,
                    "resources": [
                        {"path": f"data/{dataset_name}.parquet", "format": "parquet"}
                    ],
                }
                datapackage_path = os.path.join(temp_dir, "datapackage.yaml")
                with open(datapackage_path, "w") as dp_file:
                    yaml.dump(datapackage, dp_file)

            # Check if the repository exists
            repo_id = f"{username}/{dataset_name}"

            try:
                self._api.repo_info(repo_id=repo_id, repo_type="dataset")
                log.info(f"Repository {repo_id} exists.")
            except Exception:
                log.info(
                    f"Repository {repo_id} does not exist. Creating a new repository."
                )
                self._api.create_repo(
                    repo_id=repo_id, repo_type="dataset", private=False
                )

            # Upload the entire folder to Hugging Face
            self._api.upload_large_folder(
                folder_path=temp_dir, repo_id=repo_id, repo_type="dataset"
            )

import requests
import huggingface_hub as hf_hub
from dagster import ConfigurableResource
from datasets import Dataset, NamedSplit


class HuggingFaceResource(ConfigurableResource):
    token: str

    def login(self):
        hf_hub.login(token=self.token)

    def upload_dataset(self, dataset, name):
        self.login()
        dataset = Dataset.from_pandas(dataset, split=NamedSplit("main"))
        r = dataset.push_to_hub("davidgasquez/" + name)
        return r


class IUCNRedListAPI(ConfigurableResource):
    token: str

    def get_species(self, page):
        API_ENDPOINT = "https://apiv3.iucnredlist.org/api/v3"
        r = requests.get(f"{API_ENDPOINT}/species/page/{page}?token={self.token}")
        r.raise_for_status()

        return r.json()["result"]

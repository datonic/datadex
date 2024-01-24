import huggingface_hub as hf_hub
from dagster import ConfigurableResource, EnvVar
from datasets import Dataset


class HuggingFaceResource(ConfigurableResource):
    token: str = EnvVar("HUGGINGFACE_TOKEN")

    def login(self):
        hf_hub.login(token=self.token)

    def upload_dataset(self, dataset, name):
        self.login()
        dataset = Dataset.from_pandas(dataset)
        r = dataset.push_to_hub("davidgasquez/" + name)
        print(r)
        return r

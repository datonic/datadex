from dagster import ConfigurableResource


class HuggingFaceResource(ConfigurableResource):
    # token: str = EnvVar("HUGGINGFACE_TOKEN")

    def login(self):
        raise NotImplementedError()

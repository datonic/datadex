from frictionless import Package

from dbt.adapters.duckdb.plugins import BasePlugin


class Plugin(BasePlugin):
    def load(self, config):
        package = Package(config.meta.get("package"))
        resource_name = config.name

        if "_" in resource_name:
            resource_name = resource_name.replace("_", "-")

        resource = package.get_resource(resource_name)
        return resource.to_pandas()

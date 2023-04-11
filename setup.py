from setuptools import find_packages, setup

setup(
    name="datadex",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dbt-core",
        "dagster_dbt",
        "duckdb",
        "dbt-duckdb",
        "dbt-osmosis",
    ],
    extras_require={"dev": ["dagit"]},
)

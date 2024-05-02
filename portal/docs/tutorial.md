# Datadex Tutorial

Welcome to the Datadex tutorial! This guide will walk you through the process of adding new data sources, running dbt models, understanding the development workflow, and how Dagster integrates with dbt.

## 📦 Adding New Data Sources

Adding new data sources to Datadex involves creating a new Dagster asset. This asset is essentially a Python function that returns a DataFrame. You can fetch data from various sources as long as the function returns a DataFrame. Here's an example:

```python
@asset
def raw_owid_co2_data() -> pd.DataFrame:
    co2_owid_url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    return pd.read_csv(co2_owid_url)
```

After defining your asset, it will appear in the Dagster UI, where you can materialize it to save the resulting DataFrame to the local DuckDB database.

## 📊 Running dbt Models

With your data now in the local DuckDB database, you can start modeling it using dbt. First, ensure dbt recognizes the dataset materialized by Dagster by adding it as a source in `sources.yml`:

```yaml
version: 2
sources:
  - name: public
    tables:
      - name: raw_owid_co2_data
        meta:
          dagster:
            asset_key: ["raw_owid_co2_data"]
```

Next, create your SQL models in dbt to transform the data. For example, to select CO2 emissions data, you might write:

```sql
select country, iso_code, year, co2 from {{ source("public", "raw_owid_co2_data") }}
```

To execute this model, refresh the Dagster definitions and materialize the new dbt node, which triggers a dbt run.

## 🛠 Development Workflow

The development workflow in Datadex involves iterating between adding new sources with Dagster and modeling data with dbt. After adding a new source and materializing it, you can immediately start transforming it with dbt models. This workflow allows for rapid development and testing of data transformations.

## 🤝 Integration of Dagster with dbt

Datadex leverages the strengths of both Dagster and dbt. Dagster orchestrates the workflow, managing tasks such as fetching data, materializing assets, and triggering dbt runs. dbt focuses on transforming the data, allowing you to define models, tests, and documentation in SQL and Jinja.

Here's a practical example of how they work together:

1. Dagster fetches data from a source and materializes it as an asset in the DuckDB database.
2. A dbt model transforms this data, defined in SQL, and materializes the result.
3. Dagster can then trigger further actions based on the output of the dbt model, such as sending notifications or updating dashboards.

This integration provides a powerful framework for building and managing data pipelines in Datadex.

## 📈 Using Data

With your data modeled, you can now use it in various ways, such as in Jupyter Notebooks, BI tools, or directly querying the DuckDB database. Here's an example of querying the CO2 emissions data for visualization:

```python
import duckdb

conn = duckdb.connect("data/database.duckdb")

df = conn.execute("SELECT * FROM climate_owid_co2_by_country WHERE country = 'World'").fetchdf()
df.plot(x="year", y="co2", kind="line")
```

This concludes our tutorial on adding new sources, running dbt models, understanding the development workflow, and integrating Dagster with dbt in Datadex.

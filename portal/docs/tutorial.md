# Datadex Tutorial

Let's ingest and model some open data. We'll cover all the basics to get you started with Datadex. If you're not familiar with [dbt](https://docs.getdbt.com/) or [Dagster](Dagster), I recommend you to check their tutorials to get a sense of how these tools work.

## 📦 Adding Data Sources

The first thing is to add your desired dataset to Datadex. To do that, you'll need to create a new Dagster Asset in `assets.py`. You'll need to write a Python function that returns a DataFrame. You can do anything and read from anywhere as long as you return a DataFrame.

```python
@asset
def raw_owid_co2_data() -> pd.DataFrame:
    co2_owid_url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    return df.read_csv(co2_owid_url)
```

This will make a new asset appear in the Dagster UI (available at [localhost:3000](http://127.0.0.1:3000/) after running `make dev`). You can now select it and click "Materialize selected" to run the function and save the resulting DataFrame to our local DuckDB database.

Once the asset is materialized, you can start querying it!

## 📊 Modeling Data

Once the data is available in the local DuckDB database, you can start modeling it. You can continue using Dagster or switch to dbt. Let's explore the dbt side now.

We want to make dbt able to read the dataset Dagster materialized. To do that, we need to add a new table source to the `sources.yml`:

```yaml
version: 2
sources:
  - name: public
      - name: raw_owid_co2_data
        meta:
          dagster:
            asset_key: ["raw_owid_co2_data"]
```

Now we can create our SQL models referencing the source we just created. This is a simple query on `climate_owid_co2_by_country.sql`:

```sql
select country, iso_code, year, co2 from {{ source("public", "raw_owid_co2_data") }}
```

To run this model, we need to refresh the Dagster definitions on `Reload definitions` and materialize the new `dbt` node. That will kick off a dbt run and materialize the resulting table as parquet files (due to the `external` materialization in the `dbt_project.yml` configuration).

## 📈 Using Data

Finally, we can use the data in a notebook. Let's say we want to plot the CO2 emissions for a given country. We can use the `climate_owid_co2_by_country` table we just created:

```python
import duckdb

c = duckdb.connect("data/database.duckdb")

df = c.sql("select * from climate_owid_co2_by_country where country = 'World'").df()
_ = df.plot(x="year", y="co2", kind="line")
```

That will plot the CO2 emissions for the whole world!

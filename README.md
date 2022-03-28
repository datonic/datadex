# Datadex

Experimental project making possible to collaborate on the curation/modeling of open source datasets with `dbt` and DuckDB.

## How does it work?

Datadex is gluing together different technologies. This is how it works:

1. [Downloads some open datasets locally](Makefile). This won't be neccesary once the next `duckdb` Python release is out ([with HTTPFS enabled](https://github.com/duckdb/duckdb/issues/3243)). It'll be possible to query remote datasets from the [`sources` directory](models/sources).
2. Then, it loads them into a DuckDB Database.
3. Executes `dbt run` to build all the defined models.
4. Finally, after any changes are pushed to the `main` branch, [a GitHub Action triggers and pushes the final database as a set of parquet files to IPFS](https://github.com/davidgasquez/datadex/actions/workflows/docs.yml).

Check it out! You should be able to run a query on the final tables executing the following query on [DuckDB WASM online shell](https://shell.duckdb.org/)

This query shows the result of the [`taxi_vendors`](models/taxi_vendors.sql) model:

```sql
select
    *
from 'https://bafybeie4xkvoskx2uh6gin636htlufm7wecqagomodg5pcsvweysoryonq.ipfs.dweb.link/4_taxi_vendors.parquet';
```

You can also query the full [`raw_taxi_tripdata`](models/sources/raw_taxi_tripdata.sql) dataset using the following query:

```sql
select
    count(*)
from 'https://bafybeie4xkvoskx2uh6gin636htlufm7wecqagomodg5pcsvweysoryonq.ipfs.dweb.link/2_raw_taxi_tripdata.parquet';
```

And, [explore the final database parquet files on IPFS](https://bafybeie4xkvoskx2uh6gin636htlufm7wecqagomodg5pcsvweysoryonq.ipfs.dweb.link/).

This gives us **versioned data models** that produce **versioned datasets** on IPFS. **All automated, all open source**.

## What Works?

- Since DuckDB is using local CSV/Parquet files. It's possible to query them directly with a view. That gives you something similar to streaming data. Say that something (Airbyte/Singer/Meltano) is writting parquet files locally every hour. You can query then like this: `select * from 'data/*.parquet';`.
    - A similar thing could be done with a GitHub action crawling some data every hour and writting it to parquet files somewhere.
- Once the next version of `duckdb` Python is released, there won't be a need to get the CSV/Parquet files locally. This also mean that it'll be possible for anyone to import similar projects [as Git dbt packages](https://docs.getdbt.com/docs/building-a-dbt-project/package-management#git-packages) and build on top of them. Someone importing this repository could build a new model like this `select * from {{ ref('join') }}`.
- Have I mention a [ready to use DuckDB database is exported with each tag to IPFS](https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link/)? You can recreate the same database in any computer or browser by running `import database https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link`. Useful if you have complex views and want to start playing with them without having to copy paste a lot!
- Every release will push a new version of the database to IPFS, effectively versioning the data. A bit wasteful but might be useful if you want to keep track of all the changes and not break other projects reading from old versions.
- All the other awesome dbt features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex). E.g: [`yellow_taxi_trips.sql` documentation](https://davidgasquez.github.io/datadex/#!/model/model.datadex.yellow_taxi_trips).
- As the data is on IPFS... it should be possible to mint these datasets as NFT? Not saying is a great idea, but I feel there is something that can be done there to align incentives!

## Future

- Figure out how to best handle and export bigger datasets.
- Provide a clean URL for the versioned parquet files. Quering them should be easy. E.g: `select * from user.repo.ipfs.dweb/filename.parquet`.
- Not sure how but would be awesome to have a way to list/explore all the datasets created this way and all their versions.

## Setup

You can get started by opening this repository with VSCode Remote Containers. Once inside, you can start playing around with things like `dbt run`!

You can also run this in your browser thanks to GitHub Codespaces.

Oh! And is also possible to run visualizations on the parquet files in VSCode or Codespaces!

![1648245902](https://user-images.githubusercontent.com/1682202/160208641-0cf3e7c5-6339-408c-a08a-b5d164d1ed64.png)

## Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data+Protocol)! I just wanted to stitch together a few open source technologies and see what could they do.
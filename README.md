# Datadex

Experimental project making possible to collaborate on the curation/modeling of open source datasets with `dbt` and DuckDB.

## How does it work?

Datadex is gluing together different technologies. This is how it works:

1. [Downloads some open datasets locally](Makefile). This won't be neccesary once the next `duckdb` Python release is out ([with HTTPFS enabled](https://github.com/duckdb/duckdb/issues/3243)). It'll be possible to query remote datasets from the [`sources` directory](models/sources).
2. Then, it loads them into a DuckDB Database.
3. Executes `dbt run` to build all the defined models. [Currently it is only computing some averages and joining the two datasets](models/join.sql).
4. Finally, after any changes are pushed to the `main` branch, [a GitHub Action triggers and pushes the final database as a set of parquet files to IPFS](https://github.com/davidgasquez/datadex/actions/workflows/docs.yml).

Check it out! You should be able to run a query on the final tables executing the following query on [DuckDB WASM online shell](https://shell.duckdb.org/)


```sql
select
    *
from 'https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link/2_join.parquet';
```

This gives us **versioned data models** that produce **versioned datasets** on IPFS. **All automated, all open source**.

## What Works?

- Since DuckDB is using local CSV/Parquet files. It's possible to query them directly with a view. That gives you something similar to streaming data. Say that something (Airbyte/Singer/Meltano) is writting parquet files locally every hour. You can query then like this: `select * from 'data/*.parquet';`.
- Once the next version of `duckdb` Python is released, there won't be a need to get the CSV/Parquet files locally. This also mean that it'll be possible for anyone to import similar projects [as Git dbt packages](https://docs.getdbt.com/docs/building-a-dbt-project/package-management#git-packages) and build on top of them. Someone importing this repository could build a new model like this `select * from {{ ref('join') }}`.
- Have I mention a [ready to use DuckDB database is exported with each tag to IPFS](https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link/)? You can recreate the same database in any computer or browser by running `import database https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link`. Useful if you have complex views and want to start playing with them without having to copy paste a lot!
- Every release will push a new version of the database to IPFS, effectively versioning the data. A bit wasteful but might be useful if you want to keep track of all the changes and not break other projects reading from old versions.
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

# Datadex

Experimental project making possible to collaborate on the curation/modeling of open source datasets with `dbt` and DuckDB. This is how this MVP it works:

1. [Downloads a couple of open datasets locally](Makefile).
2. Loads them into a DuckDB Database.
3. Executes `dbt run` against it. [Currently it is only joining the two datasets](models/join.sql).
4. After any changes are pushed, [a GitHub Action triggers and pushes the final database as a set of parquet files to IPFS](https://github.com/davidgasquez/datadex/actions/workflows/docs.yml).

Check it out! You should be able to run a query on the final tables executing the following query on [DuckDB WASM online shell](https://shell.duckdb.org/)


```sql
select 
    * 
from 'https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link/2_join.parquet';
```

This gives us versioned data models that produce versioned datasets on IPFS. All automated, all open source.

## Future

Once DuckDB ships HTTPFS in their Python package, _dbt_ models could be built without having to run `dbt seed` using remote files.
Then, other projects could build on top of this project by importing it as a _dbt_ package.

## Setup

You can get started by opening this repository with VSCode Remote Containers.

Once inside, you can start playing around with things like `dbt run`!

You can also run this in your browser thanks to GitHub Codespaces.

Oh! And is also possible to visualize the models in VSCode!

![1648245902](https://user-images.githubusercontent.com/1682202/160208641-0cf3e7c5-6339-408c-a08a-b5d164d1ed64.png)


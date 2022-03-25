# Datadex

Experimental project with the goal of modeling open source data collaboratively. This is how this MVP it works:

- It takes open datasets provided by Our World in Data.
- Adds them to a DuckDB database and runs a simple join.
- One a model is commited, a GitHub Action pushed the final database as a set of parquet files to IPFS.
- These files are now available for anyone to query using [DuckDB WASM online shell](https://shell.duckdb.org/).

Check it out! You should be able to run the following query in [DuckDB WASM online shell](https://shell.duckdb.org/)


```sql
select * from 'https://bafybeialyc26ms4ollzkqxi54mdu5u4zcfecbfw4dfwuhfi25zu3k5iqpu.ipfs.dweb.link/2_join.parquet';
```

Thats it! Versioned models that give versioned datasets on IPFS. All automated, all open source.

## Setup

You can get started by opening this repository with VSCode Remote Containers.

Once inside, you can start playing around with things like `dbt run`!

You can also run this in your browser thanks to GitHub Codespaces.

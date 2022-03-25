# Datadex

Experimental project with the goal of modeling open source data collaboratively.

Currently, Datadex is pushing all the dbt modeled tables to IPFS. You can query a sample running the following query in [DuckDB WASM online shell](https://shell.duckdb.org/):

```sql
select * from 'https://bafybeidypzimyqyqjqkpciyoycdu4kfxdcha4pk24vxfmf2g5yxuvxybc4.ipfs.dweb.link/0_test.parquet';
```

All automated, all open source.

## Setup

You can get started by opening this repository with VSCode Remote Containers.

Once inside, you can start playing around with things like `dbt run`!

You can also run this in your browser thanks to GitHub Codespaces.
<p align="center">
   <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557212-c23c2bea-4179-4223-abfe-90f4a92e8aaa.png#gh-light-mode-only"/ width="400">
   <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557880-ebd4d53f-5ed8-40d2-b20c-7da90443f389.png#gh-dark-mode-only"/ width="400">

   <h4 align="center"> Model Open Data collaboratively using <a href="https://docs.getdbt.com/docs/introduction">dbt</a> and <a href="https://duckdb.org">DuckDB</a> </h4>
</p>

## What is Datadex?

Datadex is a proof of concept project to explore how people could model Open Tabular Datasets using SQL. Thanks to [dbt](https://docs.getdbt.com/docs/introduction) and [DuckDB](https://duckdb.org/) you can transform data by simply writing select statements.

### Features

- Open Data Warehouse. Run fast OLAP queries across datasets from many places (laptop, EC2, Lamdba, ...).
- Data as code. Version your SQL models and datasets.
- Package management. Publish and share your models for other people to build on top of them!
- Fully Open Source. Run everything locally.

## Usage

1. Add the [relevant sources](models/sources.yml) to the project.
1. Setup dependencies: `make deps`.
1. Execute `dbt run` to build your models.
1. Push changes to GitHub `main` branch and [a GitHub Action will trigger. It'll push the final database as a set of parquet files to IPFS](https://github.com/davidgasquez/datadex/actions/workflows/docs.yml).
1. Query and share the data! Locally, you can use Rill Developer (`make rill`). For remote data, you can use [DuckDB WASM online shell](https://shell.duckdb.org/).

This gives us **versioned data models** that produce **versioned datasets** on IPFS. **All automated, all open source**.

You can [query the `energy_yearly_averages.sql` model](https://github.com/davidgasquez/datadex/blob/main/models/energy_yearly_averages.sql) on IPFS with this query:

```sql
select
   count(*)
from 'https://bafybeieif2oj4qb4oipicjnfby555qurt4qkgy5zi57ijcsizqomfxs3gu.ipfs.dweb.link/energy_yearly_averages.parquet';
```

All [DuckDB tables are exported](https://bafybeieif2oj4qb4oipicjnfby555qurt4qkgy5zi57ijcsizqomfxs3gu.ipfs.dweb.link/) to IPFS as Parquet files too.

## What can you do with Datadex?

- Model local and remote datasets (`csv` or `parquet`) with `dbt`.
- Publish DuckDB database tables on IPFS ([example](https://bafybeieif2oj4qb4oipicjnfby555qurt4qkgy5zi57ijcsizqomfxs3gu.ipfs.dweb.link/)).
- Use any of the other awesome `dbt` features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex).
- Run visualizations on the exported parquet files thanks to the [Data Preview VS Code extension](https://github.com/RandomFractals/vscode-data-preview).
- Explore and query your models and DuckDB tables using [Rill Developer as your IDE](https://github.com/rilldata/rill-developer) (locally or via Codespaces).

| ![1](https://user-images.githubusercontent.com/1682202/160208641-0cf3e7c5-6339-408c-a08a-b5d164d1ed64.png) | ![2](https://user-images.githubusercontent.com/1682202/161124461-68864cfd-eb3a-4e4b-92f7-869d6ebcdc04.png) |
| :--------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------: |
|                                           Data Preview Extension                                           |                                             Rill Developer IDE                                             |

## Future

- Writting the exported `parquet` files to IPFS with each release is not very efficient. There might be smarter ways to handle bigger datasets (perhaps something on top of IPLD?).
- Provide a clean URL for the versioned parquet files instead of the IPFS `cid`. Quering the remote models should be something simple like `select * from user.repo.ipfs.dweb/filename.parquet`.
- Figure out a way to index datasets created this way and their versions.
- Have common packages like `dbt-countries` or `dbt-years` to enrich datasets that have a `country_code` or `year` column.

## Setup

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll need to run the following commands:
   1. `dbt deps` to download the required `dbt` packages.
   2. `dbt run-operation stage_external_sources` to instantiate views for the remote files.
   3. `dbt run` to generate your models.

PS: The development environment can also run in your browser thanks to GitHub Codespaces.

## Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data+Protocol)! I just wanted to stitch together a few open source technologies and see what could they do.

## Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/) and [dbt](https://getdbt.com).
- Datadex name was inspired by [Juan Benet awesome `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

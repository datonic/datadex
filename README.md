<p align="center">
   <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557212-c23c2bea-4179-4223-abfe-90f4a92e8aaa.png#gh-light-mode-only"/ width="400">
   <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557880-ebd4d53f-5ed8-40d2-b20c-7da90443f389.png#gh-dark-mode-only"/ width="400">

   <h4 align="center"> Model Open Data collaboratively using dbt and DuckDB </h4>
</p>

## What is Datadex?

Datadex is a proof of concept project to explore how people could model Open Tabular Datasets using SQL.

### Features

- Open Data Warehouse. Run fast OLAP queries across datasets from many places ([even from your browser](https://shell.duckdb.org/)).
- Data as code. Version your SQL models and datasets.
- Package management. Publish and share your models for other people to build on top of them!
- Fully Open Source. Run everything locally.

## Usage

1. Add the [relevant sources](models/sources.yml) to the project.
2. Execute `dbt run` to build your models.
3. Push changes to GitHub `main` branch and [a GitHub Action will trigger. It'll push the final database as a set of parquet files to IPFS](https://github.com/davidgasquez/datadex/actions/workflows/docs.yml).
4. Query and share the data! E.g: you can use [DuckDB WASM online shell](https://shell.duckdb.org/) to query the models.

This gives us **versioned data models** that produce **versioned datasets** on IPFS. **All automated, all open source**.

## What Works?

- Since DuckDB can read CSV/Parquet files. It's possible to query them directly with a view. That gives you something similar to streaming data. Say that something (Airbyte/Singer/Meltano) is writting parquet files every hour. You can query then like this: `select * from 'data/*.parquet';`.
    - A similar thing could be done with a GitHub action crawling some data every hour and writting it to parquet files somewhere.
- Have I mention a [ready to use DuckDB database is exported with each tag to IPFS](https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link/)? You can recreate the same database in any computer or browser by running `import database https://bafybeibeqezzvmxyesrub47hsacrnb3h6weghemwhlssegsvzhc7g3lere.ipfs.dweb.link`. Useful if you have complex views and want to start playing with them without having to copy paste a lot!
- Every tagged release will push a new version of the database to IPFS, effectively versioning the data. A bit wasteful but might be useful if you want to keep track of all the changes and not break other projects reading from old versions.
- All the other awesome dbt features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex). E.g: [`yellow_taxi_trips.sql` documentation](https://davidgasquez.github.io/datadex/#!/model/model.datadex.yellow_taxi_trips).
- As the data is on IPFS... it should be possible to mint these datasets as NFT? Not saying is a great idea, but I feel there is something that can be done there to align incentives!
- You can use Rill Developer as your IDE (locally or via Codespaces).
![1648735748](https://user-images.githubusercontent.com/1682202/161080067-14da939f-3b2a-4fb3-b4ff-162c179959c4.png)
- Oh! And is also possible to run visualizations on the parquet files in VSCode or Codespaces!
![1648245902](https://user-images.githubusercontent.com/1682202/160208641-0cf3e7c5-6339-408c-a08a-b5d164d1ed64.png)

## Future

- Figure out how to best handle and export bigger datasets (IPLD?).
    - Also, if someone is not building on top of a large model, it doens't make sense to instantiate it locally.
- Provide a clean URL for the versioned parquet files. Quering them should be easy. E.g: `select * from user.repo.ipfs.dweb/filename.parquet`.
- Not sure how but would be awesome to have a way to list/explore all the datasets created this way and all their versions.
- Have common packages like `dbt-countries` or `dbt-years` to enrich any datasets that have a `country_code` or `year` column.

## Setup

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you can start playing around (e.g: `dbt run`)! The development environment can also run in your browser thanks to GitHub Codespaces.

## Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data+Protocol)! I just wanted to stitch together a few open source technologies and see what could they do.

## Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/) and [dbt](https://getdbt.com).
- Datadex name was inspired by [Juan Benet awesome `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

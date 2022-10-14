<p align="center">
   <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557212-c23c2bea-4179-4223-abfe-90f4a92e8aaa.png#gh-light-mode-only"/ width="400">
   <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557880-ebd4d53f-5ed8-40d2-b20c-7da90443f389.png#gh-dark-mode-only"/ width="400">

   <h4 align="center"> Model Open Data collaboratively using <a href="https://docs.getdbt.com/docs/introduction">dbt</a> and <a href="https://duckdb.org">DuckDB</a> </h4>
</p>

## What is Datadex?

Datadex is a proof of concept project to explore how people could model Open Tabular Datasets using SQL. Thanks to [dbt](https://docs.getdbt.com/docs/introduction) and [DuckDB](https://duckdb.org/) you can transform data by simply writing select statements or import someone else's model and build on it!

### Features

- Open. Run it from your laptop, the browser, EC2...!
- Data as code. Version your datasets as dbt packages!
- Package management. Publish and share your models for other people to build on top of them!

## Usage

This is an example of how you can use Datadex to model data. Is already configured with some sample datasets. Get things working end to end with the following steps:

1. Setup dependencies with `make deps`.
1. Build your dbt models and save them to Parquet files with `make run`.
1. Explore the data with `make rill`.

## What can you do with Datadex?

- Model local and remote datasets (`csv` or `parquet`) with `dbt`.
- Use any of the other awesome `dbt` features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex).                       |

## Setup

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll only need to run `make deps`.

PS: The development environment can also run in your browser thanks to GitHub Codespaces.

## Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data+Protocol)! I just wanted to stitch together a few open source technologies and see what could they do.

## Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/) and [dbt](https://getdbt.com).
- Datadex name was inspired by [Juan Benet awesome `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

<!---
---
output-file: index
---
--->

<p align="center">
  <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557212-c23c2bea-4179-4223-abfe-90f4a92e8aaa.png#gh-light-mode-only"/ width="400">
  <img alt="Logo" src="https://user-images.githubusercontent.com/1682202/160557880-ebd4d53f-5ed8-40d2-b20c-7da90443f389.png#gh-dark-mode-only"/ width="400">

  <h4 align="center"> Collaborate on Open Data using moderns tools like <a href="https://docs.getdbt.com/docs/introduction">dbt</a> and <a href="https://duckdb.org">DuckDB</a> </h4>

  <div align="center">
    <a href='https://codespaces.new/davidgasquez/datadex'><img src='https://github.com/codespaces/badge.svg' alt='Open in GitHub Codespaces' style='max-width: 100%;'></a>
    <br>
    <a href="https://github.com/davidgasquez/datadex/actions/workflows/ci.yml"><img src="https://github.com/davidgasquez/datadex/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  </div>
</p>

## 🤔 What is Datadex?

Datadex explores how people could collaborate on Open Data using the principles and tooling from the Modern/Open Data Stack. Using tools like [dbt](https://docs.getdbt.com/docs/introduction) and [DuckDB](https://duckdb.org/) you can transform data by simply writing `select` statements or importing someone else's `model.sql` and building on top of it!

### 💡 Features

- **Open**: Play well with the rest of the ecosystem.
- **Modular**: Each tool can be replaced and extended (adapters). Works well in many environments.
- **Flexible**. Run it from your laptop, in a cluster, or from the browser.
- **Data as Code**. Version your data as code thanks to `dbt`! Publish and share your models for other people to build on top of them. Data, reproducible and accessible!
- **Modern**: Supports types, tests, materialized views, and more. Don't build new tools to work with Open Data, build bridges with the existing ones.

## 💻 Usage

This is an example of how you can use Datadex to model data. Is already configured with some sample datasets. Get things working end to end with the following steps:

1. Setup dependencies with `make deps`.
1. Build your dbt models and save them to Parquet files with `make run`.
1. Explore the data with `make rill`.

![rill](https://user-images.githubusercontent.com/1682202/195888267-ab119222-9269-4e00-98a9-8cf3a6405252.png)

## 🚀 What can you do with Datadex?

- Model local and remote datasets with `dbt`.
- Use any of the other awesome `dbt` features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex).

![docs](https://user-images.githubusercontent.com/1682202/195890290-a27498dd-1d7b-4613-ba9a-4848fb3001be.png)

## ⚙️ Setup

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll only need to run `make deps`.

PS: The development environment can also run in your browser thanks to GitHub Codespaces.

## 🎯 Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data)! I just wanted to stitch together a few open source technologies and see what could they do.

## 👏 Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/) and [dbt](https://getdbt.com).
- Datadex name was inspired by [Juan Benet awesome `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

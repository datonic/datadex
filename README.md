<!---
---
output-file: index
---
--->

<p align="center">
  <h1 style="font-size:300em;"  align="center">𝐃 𝐀 𝐓 𝐀 𝐃 𝐄 𝐗</h1>
  <p align="center"> Collaborate on Open Data using modern tools like <a href="https://docs.getdbt.com/docs/introduction">dbt</a> and <a href="https://duckdb.org">DuckDB</a> </p>
</p>


## 🤔 What is Datadex?

[![](https://github.com/davidgasquez/datadex/actions/workflows/ci.yml/badge.svg)](https://github.com/davidgasquez/datadex/actions/workflows/ci.yml)

Datadex is a set of tools and frameworks that allow everyone to collaborate on Open Data using principles from the Modern/Open Data Stack. With the help of tools like [dbt](https://docs.getdbt.com/docs/introduction) and [DuckDB](https://duckdb.org/) you can transform data by writing `select` statements.

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

![](https://user-images.githubusercontent.com/1682202/195888267-ab119222-9269-4e00-98a9-8cf3a6405252.png)

## 🚀 What can you do with Datadex?

- Model local and remote datasets with `dbt`.
- Use any of the other awesome `dbt` features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex).

![](https://user-images.githubusercontent.com/1682202/195890290-a27498dd-1d7b-4613-ba9a-4848fb3001be.png)

## ⚙️ Setup

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll only need to run `make deps`.

[![](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/datadex)

PS: The development environment can also run in your browser thanks to GitHub Codespaces.

## 🎯 Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data)! I just wanted to stitch together a few open source technologies and see what could they do.

## 👏 Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/) and [dbt](https://getdbt.com).
- Datadex name was inspired by [Juan Benet awesome `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

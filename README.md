<p align="center">
  <h1 style="font-size:80px; font-weight: 800;" align="center">D A T A D E X</h1>
  <p align="center">Collaborate on Open Data using Open Source Tools</a> </p>
</p>

<div align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/davidgasquez/datadex?style=flat-square">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/davidgasquez/datadex/ci.yml?style=flat-square">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/davidgasquez/datadex?style=flat-square">
</div>

<br>

Datadex links together tools and frameworks with the goal to allow everyone collaborate on Open Data like people collaborate on Open Source using the principles from the Open Data Stack. 

With Datadex and the help of tools like [dbt](https://docs.getdbt.com/docs/introduction) and [DuckDB](https://duckdb.org/) you can start modeling data by writing simple `select` statements!

### 💡 Principles

- **Open**: Play well with the rest of the ecosystem.
- **Modular**: Each tool can be replaced, extended, or removed. Works well in many environments ( your laptop, in a cluster, or from the browser).
- **Permissionless**. Don't ask, fork it and improve the models!
- **Data as Code**. Declarative stateless transformations tracked in `git`. Version your data as code! Publish and share your reusable models for others to build on top. Data, reproducible and accessible!
- **Modern**: Supports types, tests, materialized views, and more. Datadex isn't a new tool, it is a bridge between existing ones.

## 💻 Usage

This is an example of how you can use Datadex to model data, which is already configured with some sample datasets. Get things working end to end with the following steps:

1. Setup dependencies with `make deps`.
1. Build your dbt models and save them to Parquet files with `make run`.
1. Explore the data with `make rill`.

![](https://user-images.githubusercontent.com/1682202/195888267-ab119222-9269-4e00-98a9-8cf3a6405252.png)

## 🚀 What can you do with Datadex?

- Model local and remote datasets with `dbt`.
- Use any of the other awesome `dbt` features like `tests` and `docs`. [Docs are automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex/docs).

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

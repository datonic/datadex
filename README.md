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

Open and local friendly data platform to make Open Data collaboration easier using modular tools and frameworks.

### 💡 Principles

- **Open**: Play well with the ecosystem. Use open standards and share data in open formats.
- **Modular**: Each component can be replaced, extended, or removed. Works well in many environments (your laptop, in a cluster, or from the browser), and with multiple tools (thanks to the Arrow ecosystem).
- **Permissionless**. Don't ask, fork it and improve the models, add a new source or update any script.
- **Data as Code**. Declarative stateless transformations tracked in `git`. Version your data as code! Publish and share your reusable models for others to build on top.
- **Modern**: Supports types, tests, materialized views, and more.

Datadex is not a new tool, it is an opinionated bridge between existing ones.

### 🚀 What can you do with Datadex?

- Model [existing datasets using `Python` and `SQL` like you would do in your company](dbt/models/climate/sources.yml). You can rely on awesome `dbt` features like `tests` and `docs` ([automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex/docs)) too.
- Explore your data wherever you want. Use Jupyter Notebooks, BI Tools, Excel, .... [Share your findings with others](https://davidgasquez.github.io/datadex/notebooks/2023-05-06-quarto.html) by publishing them online as beautiful static websites (thanks to Quarto).
- Add new data sources to the Datadex. The goal is simple; bring data locally and work with it!

![Dagster Asset_Group](https://user-images.githubusercontent.com/1682202/259458000-92984525-66bc-4410-8cb0-bd1b0cbfaf1d.png)

## ⚙️ Setup

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll only need to run `make deps`.

[![](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/datadex)

PS: The development environment can also run in your browser thanks to GitHub Codespaces!

## 🎯 Motivation

This small project was created after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data)!

## 👏 Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/) and [dbt](https://getdbt.com).
- Datadex name was inspired by [Juan Benet awesome `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

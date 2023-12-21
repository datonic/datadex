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

Open source, serverless, and local-first Data Platform to collaborate on Open Data! Built on top of [Dagster](https://dagster.io/), [dbt](https://www.getdbt.com/), [Quarto](https://quarto.org/), [DuckDB](https://www.duckdb.org/), and [Evidence](https://evidence.dev/).

This repository is an up to date toy implementation of the overall pattern. You can check two real world production instances of Datadex working in the following repositories:

- [Gitcoin Grants Data Portal](https://github.com/davidgasquez/gitcoin-grants-data-portal). Improve data access and empower data scientists to conduct research and guide community driven analysis and decisions around Gitcoin Grants.
- [Filecoin Data Portal](https://github.com/davidgasquez/filecoin-data-portal/). Local-first data hub for Filecoin data! Like Dune, but in your laptop.

### 💡 Principles

- **Open**: Code, standards, infrastructure, and data, are public and open source.
- **Modular and Interoperable**: Each component can be replaced, extended, or removed. Works well in many environments (your laptop, in a cluster, or from the browser), can be deployed to many places (S3 + GH Pages, IPFS, ...) and integrates with multiple tools (thanks to the Arrow ecosystem). [Use open tool, standards, infrastructure, and share data in accesible formats](https://voltrondata.com/codex/a-new-frontier).
- **Permissionless**. Don't ask, fork it and improve the models, add a new source or update any script. No API limits, just plain files.
- **Data as Code**. Declarative stateless transformations tracked in `git`. Version your data as code! Publish and share your reusable models for others to build on top.
- **Glue**: Be a bridge between tools and aproaches. E.g: Use software engineering good practices like types, tests, materialized views, and more.

Datadex is not a new tool. **Datadex is a pattern showing an opinionated bridge between existing ones**.

### 🚀 What can you do with Datadex?

- Model [existing datasets using `Python` and `SQL` like you would do in your company](dbt/models/sources.yml). You can rely on awesome `dbt` features like `tests` and `docs` ([automatically generated and published on GitHub Pages](https://davidgasquez.github.io/datadex/dbt)) too.
- Explore your data wherever you want. Use Jupyter Notebooks, BI Tools, Excel, .... [Share your findings with others](https://davidgasquez.github.io/datadex/reports/2023-01-01-Datadex.html) by publishing them online as beautiful static websites (thanks to Quarto).
- Add new data sources to the Datadex. The goal is simple; bring data locally and work with it!

![Dagster Asset_Group](https://user-images.githubusercontent.com/1682202/259458000-92984525-66bc-4410-8cb0-bd1b0cbfaf1d.png)

## ⚙️ Setup

Datadex consists of several components and requires some setup to get started.

### 🐳 Docker / Dev Containers

The fastest way to start using Datadex is via [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers). Once inside the develpment environment, you'll only need to run `make dev` to spin up the [Dagster UI locally](http://127.0.0.1:3000).

[![](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/datadex)

The development environment can also run in your browser thanks to GitHub Codespaces!

You can also build the [Dockerfile](Dockerfile) image locally and run it with:

```bash
docker build -t datadex .
docker run -it -v $(pwd):/workspaces/datadex -p 3000:3000 datadex
```

### 🐍 Python Virtual Environment

Clone the repository and run the following commands from the root folder:

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the package and dependencies
pip install -e .[dev]
```

Now, you should be able to spin up Dagster UI and [access it locally](http://127.0.0.1:3000).

## 🎯 Motivation

This project started after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data)!

## 👏 Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/), [dbt](https://getdbt.com), [Dagster](https://dagster.io/), and [Quarto](https://quarto.org/).
- Datadex name was inspired by [Juan Benet's `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

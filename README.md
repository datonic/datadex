<p align="center">
  <h1 style="font-size:80px; font-weight: 800;" align="center">D A T A D E X</h1>
  <p align="center">A Data Platform for your community Open Data</a> </p>
</p>

<div align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/davidgasquez/datadex?style=flat-square">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/davidgasquez/datadex/ci.yml?style=flat-square">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/davidgasquez/datadex?style=flat-square">
</div>

<br>

Datadex is a fully open-source, serverless, and local-first Data Platform that improves how communities collaborate on Open Data. Datadex is not a new tool, it is a pattern showing an opinionated bridge between existing ones.

You can check two real-world production implementation of the Datadex pattern working in the following repositories:

- [Gitcoin Grants Data Portal](https://github.com/davidgasquez/gitcoin-grants-data-portal). Data hub for Gitcoin Grants data. Improves data access and empowers data scientists to conduct research and helps to guide community-driven analysis and decisions.
- [Arbitrum Grants Data Portal](https://github.com/davidgasquez/arbitrum-data-portal).  Data hub for Arbitrum Grants data.  Improves data access and empowers data scientists to conduct research and helps to guide community-driven analysis and decisions.
- [Filecoin Data Portal](https://github.com/davidgasquez/filecoin-data-portal/). Data hub for Filecoin data! Like Dune, but in your laptop.

### 💡 Principles

- **Open**: Code, standards, infrastructure, and data, are public and open source.
- **Modular and Interoperable**: Each component can be replaced, extended, or removed. Works well in many environments (your laptop, in a cluster, or from the browser), can be deployed to many places (S3 + GH Pages, IPFS, ...) and integrates with multiple tools (thanks to the Arrow ecosystem). [Use open tool, standards, infrastructure, and share data in accesible formats](https://voltrondata.com/codex/a-new-frontier).
- **Permissionless**. Don't ask, fork it and improve the models, add a new source or update any script. No API limits, just plain files.
- **Data as Code**. Declarative stateless transformations tracked in `git`. Version your data as code! Publish and share your reusable models for others to build on top. Datasets should be both reproducible and accessible!
- **Glue**: Be a bridge between tools and aproaches. E.g: Use software engineering good practices like types, tests, materialized views, and more.

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

<p align="center">
  <h1 style="font-size:80px; font-weight: 800;" align="center">D A T A D E X</h1>
  <p align="center">The Open Data Platform for your community Open Data</a> </p>
</p>

<div align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/davidgasquez/datadex?style=flat-square">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/davidgasquez/datadex/ci.yml?style=flat-square">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/davidgasquez/datadex?style=flat-square">
</div>

<br>

Datadex is a fully open-source, serverless, and local-first Data Platform that improves how communities collaborate on Open Data. Datadex is not a new tool, it is a pattern showing an opinionated bridge between existing ones.

You can [learn more about the approach in this post](https://davidgasquez.com/modern-open-data-portals/) or check other real-world production implementations of the Datadex pattern working in the following repositories:

- [Gitcoin Grants Data Portal](https://github.com/davidgasquez/gitcoin-grants-data-portal). Data hub for Gitcoin Grants data. Improves data access and empowers data scientists to conduct research and helps to guide community-driven analysis and decisions.
- [Arbitrum Grants Data Portal](https://github.com/davidgasquez/arbitrum-data-portal).  Data hub for Arbitrum Grants data.  Improves data access and empowers data scientists to conduct research and helps to guide community-driven analysis and decisions.
- [Filecoin Data Portal](https://github.com/davidgasquez/filecoin-data-portal/). Data hub for Filecoin data! Like Dune, but in your laptop.

![Global_Asset_Lineage](https://github.com/datonic/datadex/assets/1682202/5734a6b9-0618-4bf6-958a-1c45f5d34442)

### 💡 Principles

- **Open**: Code, standards, infrastructure, and data, are public and open source.
- **Modular and Interoperable**: Each component can be replaced, extended, or removed. Works well in many environments (your laptop, in a cluster, or from the browser), can be deployed to many places (S3 + GH Pages, IPFS, ...) and integrates with multiple tools (thanks to the Arrow ecosystem). [Use open tool, standards, infrastructure, and share data in accesible formats](https://voltrondata.com/codex/a-new-frontier).
- **Permissionless**. Don't ask, fork it and improve the models, add a new source or update any script. No API limits, just plain files.
- **Data as Code**. Declarative stateless transformations tracked in `git`. Improves data access and empowers data scientists to conduct research and helps to guide community-driven analysis and decisions.ersion your data as code! Publish and share your reusable models for others to build on top. Datasets should be both reproducible and accessible!
- **Glue**: Be a bridge between tools and aproaches. E.g: Use software engineering good practices like types, tests, materialized views, and more.

### 🚀 What can you do with Datadex?

- Add new data sources. Bring data locally and work with it!
- Model existing datasets using `Python` and `SQL`.
- Explore your data wherever you want. Use Jupyter Notebooks, BI Tools, Excel, ....
- [Share your findings with others](https://datadex.datonic.io/notebooks/2023-01-01-Datadex) by publishing them online as beautiful static websites.

## ⚙️ Setup

There are two ways to get started with Datadex or your own Open Data Portal/Platform based on the Datadex pattern, Python Virtual Environment or Docker / Dev Containers.

If you hit any issue, please [open an issue](https:github.com/datonic/datadex/issues/new)!

### 🐍 Python Virtual Environment

You can install all the dependencies inside a Python virtual environment by running `make setup`. To do that, clone the repository and run the following commands from the root folder.

```bash
make setup
```

Alternatively, you can rely on your system's Python installation to create a virtual environment and install the dependencies.

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the package and dependencies
pip install -e ".[dev]"
```

Now, you should be able to spin up Dagster UI (`make dev` or `dagster dev`) and [access it locally](http://127.0.0.1:3000).

### 🐳 Docker / Dev Containers

Using [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers) is the fastest and smoother way to start using Datadex, but requires you to have Docker running. Open the project in VSCode and click on the bottom right corner to open the project in a container.

Once inside the develpment environment, you'll only need to run `make dev` to spin up the [Dagster UI locally](http://127.0.0.1:3000). You'll also have a few extra extensions installed and configured to work with the project.

The development environment can also run in your browser thanks to GitHub Codespaces!

[![badge](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/datadex)

## 🎯 Motivation

This project started after [thinking how an Open Data Protocol could look like](https://publish.obsidian.md/davidgasquez/Open+Data)!

## 👏 Acknowledgements

- This proof of concept was created thanks to open source projects like [DuckDB](https://www.duckdb.org/), [dbt](https://getdbt.com), [Dagster](https://dagster.io/), [Quarto](https://quarto.org/), ...
- Datadex name was inspired by [Juan Benet's `data` projects](https://juan.benet.ai/blog/2014-03-11-discussion-scienceexchange/).

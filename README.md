<p align="center">
  <h1 style="font-size:80px; font-weight: 800;" align="center">D A T A D E X</h1>
  <p align="center">The Open Data Platform for your community Open Data</a> </p>
</p>

<div align="center">
  <img alt="GitHub" src="https://img.shields.io/github/license/davidgasquez/datadex?style=flat-square">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/davidgasquez/datadex/etl.yml?style=flat-square">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/davidgasquez/datadex?style=flat-square">
</div>

<br>

Datadex is a fully open-source, serverless, and local-first Data Platform that improves how communities collaborate on Open Data. Datadex is not a new tool, it is a pattern showing an opinionated bridge between existing ones.

[You can learn more about this approach in this post](https://davidgasquez.com/modern-open-data-portals/) or check other real-world production implementations of the Datadex pattern working in the following repositories:

- [LUNG-SARG](https://github.com/open-radiogenomics/lung-sarg). The Open Data Platform for Sustainable, Accessible Lung Radiogenomics.
- [Datania](https://github.com/davidgasquez/datania/). An Open Data Platform at national level that unifies and harmonizes information from different sources.
- [Gitcoin Grants Data Portal](https://github.com/davidgasquez/gitcoin-grants-data-portal). A Data hub for Gitcoin Grants data and related models.
- [Filecoin Data Portal](https://github.com/davidgasquez/filecoin-data-portal/). A data portal for data related to the Filecoin network and ecosystem.

### 💡 Principles

- **Open**: Code, standards, infrastructure, and data, are public and open source.
- **Modular and Interoperable**: Each component can be replaced, extended, or removed. Works well in many environments (your laptop, in a cluster, or from the browser), can be deployed to many places (S3 + GH Pages, IPFS, Hugging Face) and integrates with multiple tools. Uses open tools, standards, infrastructure, and shares data in [accessible formats](https://voltrondata.com/codex/a-new-frontier).
- **Permissionless**: Fork it and improve the pipelines, datasets, or documentation. Datasets are published as static files. No API limits, just plain files.
- **Data as Code**: Datasets are reproducible thanks to declarative stateless transformations tracked in `git`. Improves data access and empowers data scientists to conduct research and helps to guide community-driven analysis and decisions. Data is versioned alongside the code. Publish and share your reusable models for others to build on top.
- **Glue**: Be a bridge between tools and approaches. E.g: Use software engineering good practices like types, tests, materialized views, and more.

## ⚙️ Setup

Datadex is mainly a Python project, so you'll need to have Python installed. If you hit any issue, please [open an issue](https:github.com/datonic/datadex/issues/new)! The easiest way to get started is using a Python virtual environment, but a development container is also provided.

### 🐍 Python Virtual Environment

The recommended way is to install [`uv`](https://github.com/astral-sh/uv) and let it manage the Python environment. The following commands will install the dependencies and create a virtual environment in the project's folder.

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

You can use [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers) to get started with Datadex too. If you have Docker running, open the project in VSCode and click on the bottom right corner to open the project in a container.

Once inside the develpment environment, you'll only need to run `make dev` to spin up the [Dagster UI locally](http://127.0.0.1:3000). You'll also have a few extra extensions installed and configured to work with the project.

The development environment can also run in your browser thanks to GitHub Codespaces!

[![badge](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/datadex)

## 📜 License

Datadex is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

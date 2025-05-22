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

Datadex is a fully open-source, serverless, and local-first Data Platform to improve how [communities collaborate on Open Data](https://davidgasquez.com/community-level-open-data-infrastructure/). Why?

- Increase your community's coordination and shared understanding.
- Makes it easy to publish data products built by your community, for your community.

## 🚀 Implementations

Check other [real-world production Open Data Portals](https://davidgasquez.com/modern-open-data-portals/) of the Datadex pattern in the following repositories:

- [LUNG-SARG](https://github.com/open-radiogenomics/lung-sarg). The Open Data Platform for Sustainable, Accessible Lung Radiogenomics.
- [Datania](https://github.com/davidgasquez/datania/). An Open Data Platform at national level that unifies and harmonizes information from different sources.
- [Gitcoin Grants Data Portal](https://github.com/davidgasquez/gitcoin-grants-data-portal). A Data hub for Gitcoin Grants data and related models.
- [Filecoin Data Portal](https://github.com/davidgasquez/filecoin-data-portal/). A data portal for data related to the Filecoin network and ecosystem.

## 💡 Principles

> [Make Open Data compatible with the Modern Data Ecosystem](https://handbook.davidgasquez.com/Open+Data).

- **Open**: Code, standards, infrastructure, and data, all public and open source. Rely on open source tools, standards, public infrastructure, and [accessible data formats](https://voltrondata.com/codex/a-new-frontier).
- **Modular and Interoperable**: Easy to replace, extend or remove components of the pattern. Environment flexibility (your laptop, in a cluster, or from the browser) when running and when deploying (S3 + GH Pages, IPFS, Hugging Face).
- **Permissionless**: Any improvement is one Pull Request away. Update pipelines, add datasets, or improve documentation. When consuming, there are no API limits, just plain files.
- **Data as Code**: Reproducible datasets with declarative stateless transformations tracked in `git`. Data is versioned alongside the code.
- **Glue**: Be a bridge between tools and approaches. E.g: Use software engineering good practices like types, tests, materialized views, and more.

## ⚙️ Setup

Datadex is a Python project. The easiest way to get started is using a Python virtual environment.

If you hit any issue, please [open an issue](https:github.com/datonic/datadex/issues/new)!

### 🐍 Python Virtual Environment

Install [`uv`](https://github.com/astral-sh/uv) and let it manage the Python environment. The following commands will install the dependencies.

```bash
make setup
```

Alternatively, you can rely on your system's Python installation to create a virtual environment and install the dependencies.

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the package and dependencies
pip install -e .
```

### 🐳 Docker / Dev Containers

You can use [VSCode Remote Containers](https://code.visualstudio.com/docs/remote/containers) to get started with Datadex too. If you have Docker installed and running, open the project in VSCode and click on the bottom right corner to open the project in a container.

The development environment can also run in your browser thanks to GitHub Codespaces!

[![badge](https://github.com/codespaces/badge.svg)](https://codespaces.new/davidgasquez/datadex)

## 📜 License

Datadex is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

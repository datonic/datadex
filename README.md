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

Open-source, serverless, and local-first data platform for your community. Datadex helps [communities collaborate on Open Data](https://davidgasquez.com/community-level-open-data-infrastructure/), increasing the community's coordination and shared understanding by making it easy to build and publish data products, by your community, for your community.

> [!NOTE]
> The previous version of Datadex, which utilized Dagster and DuckDB, can be found at [this commit](https://github.com/datonic/datadex/tree/e0906b943bb35a4507fa24aa33494e9d7ceb6fef).

## 🚀 Implementations

Datadex is a pattern, not only a project. Check [real-world production Open Data Portals](https://davidgasquez.com/modern-open-data-portals/) based on Datadex:

- [Datania](https://github.com/davidgasquez/datania/). Open Data Platform that unifies and harmonizes information relevant Spanish datasets from different sources.
- [Filecoin Data Portal](https://github.com/davidgasquez/filecoin-data-portal/). The main open data portal around the Filecoin ecosystem.
- [LUNG-SARG](https://github.com/open-radiogenomics/lung-sarg). Open Data Platform for Sustainable, Accessible Lung Radiogenomics.
- [Gitcoin Grants Data Portal](https://github.com/davidgasquez/gitcoin-grants-data-portal). A Data hub for Gitcoin Grants data and related models.

## 💡 Principles

> [Make working with open data easy and accessible by using modern tooling and approaches](https://handbook.davidgasquez.com/Open+Data).

- **Open**: Code, standards, infrastructure, and data, all public and open source. Rely on open source tools, standards, public infrastructure, and [accessible data formats](https://voltrondata.com/codex/a-new-frontier).
- **Modular and Interoperable**: Easy to replace, extend or remove components of the pattern. Environment flexibility (laptop, cluster, browser) when running and when deploying (S3 + GH Pages, IPFS, Hugging Face).
- **Permissionless**: Any improvement is one Pull Request away. Update pipelines, add datasets, or improve documentation. No API limits, just plain open files.
- **Simple**: Static assets, batch jobs.
- **Data as Code**: Reproducible datasets with declarative stateless transformations tracked in `git`. Data is versioned alongside the code.
- **Glue**: Be a bridge between tools and approaches. Follow UNIX philosophy.

## ⚙️ Setup

You can get started easily by setting up a Python virtual environment. If you hit any issue, please [open an issue](https://github.com/datonic/datadex/issues/new)!

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

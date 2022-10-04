FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

RUN apt-get update && apt-get install -y nodejs npm g++

# Install dbt
RUN pip3 --disable-pip-version-check --no-cache-dir install duckdb==0.5.0 dbt-duckdb==1.2.1 \
    && rm -rf /tmp/pip-tmp

# Install duckdb cli
RUN wget https://github.com/duckdb/duckdb/releases/download/v0.5.1/duckdb_cli-linux-amd64.zip \
    && unzip duckdb_cli-linux-amd64.zip -d /usr/local/bin \
    && rm duckdb_cli-linux-amd64.zip

# Configure Workspace
ENV DBT_PROFILES_DIR=/workspaces/datadex
WORKDIR /workspaces/datadex

# Install Rill Developer
RUN curl -s https://cdn.rilldata.com/install.sh | bash

# Setup IPFS
RUN cd /tmp && wget https://dist.ipfs.io/kubo/v0.15.0/kubo_v0.15.0_linux-amd64.tar.gz \
    && tar -xvzf kubo_v0.15.0_linux-amd64.tar.gz \
    && cd kubo && bash install.sh

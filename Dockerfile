FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

RUN apt-get update && apt-get install -y nodejs npm g++

# Install dbt
RUN pip3 --disable-pip-version-check --no-cache-dir install duckdb==0.4.0 dbt-duckdb==1.1.4 \
    && rm -rf /tmp/pip-tmp

# Install duckdb cli
RUN wget https://github.com/duckdb/duckdb/releases/download/v0.4.0/duckdb_cli-linux-amd64.zip \
    && unzip duckdb_cli-linux-amd64.zip -d /usr/local/bin \
    && rm duckdb_cli-linux-amd64.zip

# Configure Workspace
ENV DBT_PROFILES_DIR=/workspaces/datadex
WORKDIR /workspaces/datadex

# Install Rill Developer
RUN wget https://github.com/rilldata/rill-developer/releases/download/v0.7.0/rill-linux-x64 && \
    chmod +x rill-linux-x64 && \
    mv rill-linux-x64 /usr/local/bin/rill

# Setup IPFS
RUN cd /tmp && wget https://dist.ipfs.io/go-ipfs/v0.12.2/go-ipfs_v0.12.2_linux-amd64.tar.gz \
    && tar -xvzf go-ipfs_v0.12.2_linux-amd64.tar.gz \
    && cd go-ipfs && bash install.sh

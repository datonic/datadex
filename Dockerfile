FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get -y install --no-install-recommends \
    build-essential aria2 zstd

# Install Quarto
RUN curl -sL $(curl https://quarto.org/docs/download/_prerelease.json | grep -oP "(?<=\"download_url\":\s\")https.*${ARCH}\.deb") --output /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb

# Configure Workspace
WORKDIR /workspaces/datadex
ENV DBT_PROFILES_DIR=/workspaces/datadex/dbt
ENV DAGSTER_HOME=/home/vscode/
ENV DATA_DIR=/workspaces/datadex/data

# Add files to workspace
COPY . /workspaces/datadex

# Install Python Dependencies
RUN pip install -e ".[dev]"

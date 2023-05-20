FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && apt-get -y install --no-install-recommends \
    build-essential aria2 zstd

# Install Quarto
RUN curl -sL $(curl https://quarto.org/docs/download/_prerelease.json | grep -oP "(?<=\"download_url\":\s\")https.*${ARCH}\.deb") --output /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb


# Install npm (for Evidence)
# RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - \
#     && apt-get install -y nodejs

# Configure Workspace
WORKDIR /workspaces/datadex
ENV DBT_PROFILES_DIR=/workspaces/datadex/dbt
ENV DAGSTER_HOME=/home/vscode/

# Install Python Dependencies
COPY . /workspaces/datadex
RUN pip install -e ".[dev]"

# Install Rill Developer
RUN curl -s https://cdn.rilldata.com/install.sh | bash

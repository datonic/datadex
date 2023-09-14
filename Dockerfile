FROM mcr.microsoft.com/devcontainers/python:3

# Install base packages
RUN apt-get update && apt-get -y install --no-install-recommends \
    build-essential aria2 zstd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN curl -sL $(curl https://quarto.org/docs/download/_download.json | grep -oP "(?<=\"download_url\":\s\")https.*${ARCH}\.deb") --output /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb

# Workspace Folder
ENV WORKSPACE_FOLDER=/workspaces/datadex
WORKDIR $WORKSPACE_FOLDER

# Configure Environment
ENV DBT_PROFILES_DIR=$WORKSPACE_FOLDER/dbt
ENV DATA_DIR=$WORKSPACE_FOLDER/data
ENV DAGSTER_HOME=/home/vscode/

# Add files to workspace
COPY . $WORKSPACE_FOLDER

# Install Python Dependencies
RUN pip install -e ".[dev]"

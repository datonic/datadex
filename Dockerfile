FROM mcr.microsoft.com/devcontainers/python:3.11

# Install base packages
RUN apt-get update && apt-get -y install --no-install-recommends \
    build-essential aria2 zstd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN curl -sL $(curl https://quarto.org/docs/download/_prerelease.json | grep -oP "(?<=\"download_url\":\s\")https.*${ARCH}\.deb") --output /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb

# Workspace Folder
ENV WORKSPACE_FOLDER=/workspaces/datadex
WORKDIR $WORKSPACE_FOLDER

# Copy Files
COPY datadex $WORKSPACE_FOLDER/datadex
COPY dbt $WORKSPACE_FOLDER/dbt
COPY pyproject.toml $WORKSPACE_FOLDER

# Install Python Dependencies
RUN pip install -e ".[dev]"

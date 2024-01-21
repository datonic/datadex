FROM mcr.microsoft.com/devcontainers/python:3.11

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash

# Install base packages
RUN apt-get update && apt-get -y install --no-install-recommends \
    build-essential aria2 zstd nodejs \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto
RUN curl -sL $(curl https://quarto.org/docs/download/_prerelease.json | grep -oP "(?<=\"download_url\":\s\")https.*${ARCH}\.deb") --output /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb

# Environment Variables
ENV DAGSTER_HOME "/home/vscode"

# Working Directory
WORKDIR /workspaces/datadex

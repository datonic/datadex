FROM mcr.microsoft.com/devcontainers/python:3.11

# Install base packages
RUN apt-get update && apt-get -y install --no-install-recommends \
    build-essential aria2 zstd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Node.js
# RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash && \
#     export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")" \
#     [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
#     nvm install node

# Install Quarto
RUN curl -sL $(curl https://quarto.org/docs/download/_prerelease.json | grep -oP "(?<=\"download_url\":\s\")https.*${ARCH}\.deb") --output /tmp/quarto.deb \
    && dpkg -i /tmp/quarto.deb \
    && rm /tmp/quarto.deb

# Environment Variables
ENV DAGSTER_HOME "/home/vscode"

# Working Directory
WORKDIR /workspaces/datadex

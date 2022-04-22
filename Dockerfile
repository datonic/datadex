FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

RUN apt-get update && apt-get install -y nodejs npm

RUN pip3 --disable-pip-version-check --no-cache-dir install duckdb dbt-duckdb \
    && rm -rf /tmp/pip-tmp

ENV DBT_PROFILES_DIR=/workspaces/datadex
WORKDIR /workspaces/datadex

USER vscode

RUN curl -fsSL https://deb.nodesource.com/setup_current.x | sudo bash - && sudo apt-get install -y nodejs
RUN git clone https://github.com/rilldata/rill-developer.git /home/vscode/rill-developer && cd /home/vscode/rill-developer && npm install && npm run build

ENTRYPOINT "/bin/bash"
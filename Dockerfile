FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

RUN pip3 --disable-pip-version-check --no-cache-dir install dbt-duckdb \
    && rm -rf /tmp/pip-tmp

ENV DBT_PROFILES_DIR=/workspaces/datadex
WORKDIR /workspaces/datadex

ENTRYPOINT "/bin/bash"
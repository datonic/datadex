FROM mcr.microsoft.com/devcontainers/python:3.10

RUN apt-get update && apt-get install -y nodejs npm g++

# Install dbt
RUN pip3 --disable-pip-version-check --no-cache-dir install \
    duckdb==0.6.1 dbt-duckdb==1.3.4 dbt-osmosis==0.9.8 \
    && rm -rf /tmp/pip-tmp

# Configure Workspace
WORKDIR /workspaces/datadex
ENV DBT_PROFILES_DIR=/workspaces/datadex

# Install Rill Developer
RUN wget https://github.com/rilldata/rill-developer/releases/download/v0.20.0/rill_linux_amd64.zip -O /tmp/rill_linux_amd64.zip \
    && unzip /tmp/rill_linux_amd64.zip rill -d /usr/local/bin \
    && chmod +x /usr/local/bin/rill \
    && rm /tmp/rill_linux_amd64.zip

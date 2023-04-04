FROM mcr.microsoft.com/devcontainers/python:3.10

RUN apt-get update && apt-get install -y make

# Install dbt
RUN pip3 --disable-pip-version-check --no-cache-dir install \
    duckdb==0.7.1 dbt-duckdb==1.4.1 dbt-osmosis==0.11.17 \
    && rm -rf /tmp/pip-tmp

# Configure Workspace
WORKDIR /workspaces/datadex
ENV DBT_PROFILES_DIR=/workspaces/datadex

# Install Rill Developer
RUN wget https://github.com/rilldata/rill-developer/releases/download/v0.23.1/rill_linux_amd64.zip -O /tmp/rill_linux_amd64.zip \
    && unzip /tmp/rill_linux_amd64.zip rill -d /usr/local/bin \
    && chmod +x /usr/local/bin/rill \
    && rm /tmp/rill_linux_amd64.zip

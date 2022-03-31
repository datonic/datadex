FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Build DuckDB Python with HTTPFS Support
RUN pip install --prefer-binary pandas pytest
RUN git clone https://github.com/duckdb/duckdb
RUN apt-get update -y -qq && apt-get install -y git ninja-build make gcc-multilib g++-multilib wget libssl-dev
RUN wget https://github.com/Kitware/CMake/releases/download/v3.21.3/cmake-3.21.3-linux-x86_64.sh && chmod +x cmake-3.21.3-linux-x86_64.sh && ./cmake-3.21.3-linux-x86_64.sh --skip-license --prefix=/usr/local
RUN cd /duckdb && GEN=ninja DISABLE_MAIN_DUCKDB_LIBRARY=1 BUILD_HTTPFS=1 STATIC_OPENSSL=1 make
RUN cd /duckdb/tools/pythonpkg && python setup.py sdist && pip install -e .

RUN apt-get update && apt-get install -y nodejs npm
RUN curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && apt-get install -y nodejs
RUN git clone https://github.com/rilldata/rill-developer.git /home/vscode/rill-developer && cd /home/vscode/rill-developer && npm install && npm run build

RUN pip install dbt-duckdb
RUN echo "$(echo -n 'import sys, os; sys.setdlopenflags(os.RTLD_GLOBAL | os.RTLD_NOW);'; cat /usr/local/lib/python3.9/site-packages/dbt/adapters/duckdb/connections.py)" > /usr/local/lib/python3.9/site-packages/dbt/adapters/duckdb/connections.py

# This is how it'll run once upstread is fixed
# RUN pip3 --disable-pip-version-check --no-cache-dir install dbt-duckdb \
#     && rm -rf /tmp/pip-tmp

ENV DBT_PROFILES_DIR=/workspaces/datadex
WORKDIR /workspaces/datadex

ENTRYPOINT "/bin/bash"
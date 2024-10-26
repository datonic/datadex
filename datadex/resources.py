import os

import dagster as dg
from dagster_duckdb_polars import DuckDBPolarsIOManager

log = dg.get_dagster_logger()

DATABASE_PATH = os.getenv("DATABASE_PATH", "data/database.duckdb")
io_manager = DuckDBPolarsIOManager(database=DATABASE_PATH, schema="main")

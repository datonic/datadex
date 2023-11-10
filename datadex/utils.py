import os

import duckdb

db_dir = os.path.dirname(os.path.abspath(__file__)) + "/../data/"


def custom_f():
    return 42


def query(sql):
    with duckdb.connect(database=f"{db_dir}/local.duckdb") as con:
        return con.sql(sql).df()

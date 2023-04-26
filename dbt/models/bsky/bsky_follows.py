import os
import urllib.request

import duckdb


def model(dbt, session):
    # Download the database if it doesn't exist
    if not os.path.exists("../data/bsky.db"):
        urllib.request.urlretrieve(
            "https://huggingface.co/datasets/andrewconner/bluesky_profiles/resolve/main/bsky.db",
            "../data/bsky.db",
        )

    duckdb.sql(
        """
        INSTALL sqlite_scanner;
        LOAD sqlite_scanner;
        """
    )

    q = duckdb.sql(
        """
        select * from sqlite_scan('../data/bsky.db', 'follows')
        """
    )

    return q.to_arrow_table()

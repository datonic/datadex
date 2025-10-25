import inspect
from collections.abc import Callable
from pathlib import Path

import polars as pl


def materialize(dataset_fn: Callable[[], pl.DataFrame]) -> Path:
    """Persist dataset_fn() to <script-dir>/data/<function>.parquet."""

    # Directory of the file where the callable is defined; fall back to CWD if unknown.
    source_file = inspect.getsourcefile(dataset_fn)
    base_dir = Path(source_file).resolve().parent if source_file else Path.cwd()

    function_name = getattr(dataset_fn, "__name__", dataset_fn.__class__.__name__)
    output_path = base_dir / "data" / f"{function_name}.parquet"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = dataset_fn()
    if not isinstance(df, pl.DataFrame):
        raise TypeError(
            f"Dataset callable must return a polars.DataFrame, got {type(df)!r} instead."
        )

    df.write_parquet(output_path, compression="zstd", statistics=True)
    return output_path

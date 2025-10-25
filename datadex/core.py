from __future__ import annotations

import inspect
import warnings
from collections.abc import Callable
from pathlib import Path

import httpx
import polars as pl


def materialize(dataset_fn: Callable[[], pl.DataFrame]) -> Path:
    """Persist the result of a dataset callable to the data directory.

    The output path is derived from the module filename and the callable name,
    following the ``data/<filename>/<function>.parquet`` convention.
    """

    dataset_path = _output_path(dataset_fn)
    dataset_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe = dataset_fn()
    if not isinstance(dataframe, pl.DataFrame):
        msg = (
            "Dataset callable must return a polars.DataFrame, "
            f"got {type(dataframe)!r} instead."
        )
        raise TypeError(msg)

    dataframe.write_parquet(dataset_path, compression="zstd", statistics=True)
    return dataset_path


def fetch_bytes(
    url: str,
    *,
    timeout: float | httpx.Timeout = 120.0,
    follow_redirects: bool = True,
) -> bytes:
    """Download the content at ``url`` and return the raw bytes.

    The request is attempted with standard TLS verification. If that fails due to
    certificate validation errors (common behind corporate proxies), a single
    retry is performed with verification disabled while emitting a warning.
    """

    headers = {"User-Agent": "datadex/0.1"}

    try:
        response = httpx.get(
            url,
            follow_redirects=follow_redirects,
            timeout=timeout,
            headers=headers,
        )
    except httpx.HTTPError as exc:
        if "CERTIFICATE_VERIFY_FAILED" not in repr(exc):
            raise

        warnings.warn(
            f"Falling back to insecure TLS download for {url}",
            RuntimeWarning,
            stacklevel=2,
        )
    else:
        response.raise_for_status()
        return response.content

    response = httpx.get(
        url,
        follow_redirects=follow_redirects,
        timeout=timeout,
        headers=headers,
        verify=False,
    )
    response.raise_for_status()
    return response.content


def _output_path(dataset_fn: Callable[[], pl.DataFrame]) -> Path:
    source_file = inspect.getsourcefile(dataset_fn)
    if source_file is not None:
        module_name = Path(source_file).stem
    else:
        module_name = str(getattr(dataset_fn, "__module__", "dataset").split(".")[-1])

    function_name = str(getattr(dataset_fn, "__name__", dataset_fn.__class__.__name__))
    return Path("data") / module_name / f"{function_name}.parquet"

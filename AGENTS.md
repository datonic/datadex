# Contributing

Guidance when contributing to the Datadex project.

## Development

Check the [README](README.md) for how to get started. The [Makefile](Makefile) contains common commands to run, lint, test, etc.

## Architecture

Datadex is a minimalistic and functional open data platform to help communities get, transform and publish open data.

### Data Pipeline Architecture

- Simple and functional.
- Low abstractions, no frameworks.
- Each file is a self-contained dataset.
- Rely on Makefile for orchestration.
- Datasets are stored in the `data/` directory.

```python
import polars as pl
from pathlib import Path

def A(dep: pl.DataFrame) -> pl.DataFrame:
    return dep.with_columns(A = pl.col("x") * 10).select("A")

if __name__ == "__main__":
    dep = pl.read_parquet("data/source.parquet")
    res = A(dep)
    Path("data").mkdir(exist_ok=True)
    res.write_parquet("data/A.parquet", complression="zstd", statistics=True)
    print("✅ A.parquet written")
```

### Deployment Strategy

- Datasets are uploaded to Hugging Face Datasets (`datonic` organization).
- API is deployed as Hugging Face Space using Docker.
- Web interface served statically from `web/` directory.
- Everything versioned in git following "data as code" principles.

## Key Dependencies

- **Polars**: Primary data processing library.
- **httpx**: HTTP client for data fetching.
- **pyarrow**: Parquet file handling.
- **uv**: Python package and environment management.

# Contributing

Guidance when contributing to Datadex.

## Development

Check the [README](README.md) for how to get started. The [Makefile](Makefile) contains common commands.

## Architecture

Datadex is a serverless and local friendly open data platform that helps communities and organizations to get, transform and publish open data.

### Data Pipeline Architecture

- **ETL modules**: Individual Python scripts that fetch, transform, and save datasets.
- **Data output** (`data/`): Generated Parquet files optimized with ZSTD compression and statistics

### Core Data Processing Pattern

The pipelines should be simple and self-contained. The output should be a Parquet file with the name of the file being the name of the dataset.

These steps should be followed:

1. Each dataset module fetches raw data from public sources.
2. Data is transformed using Polars/DuckDB for efficient processing.
3. Output is sorted by key columns (e.g; `country_code/iso_code`, `year`) for query optimization.
4. Parquet files use v2 format with ZSTD compression and statistics enabled.

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

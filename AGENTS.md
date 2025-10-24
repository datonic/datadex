# Contributing

Guidance when contributing to the Datadex project.

## Development

Check the [README](README.md) for how to get started. The [Makefile](Makefile) contains common commands to run, lint, test, etc.

## Architecture

Datadex is a minimalistic and functional open data platform to help communities get, transform and publish open data.

### Principles

- Simple and functional.
- Low abstractions, no frameworks.
- UNIX philosophy.
- One file, one dataset.
- Datasets are stored in the `data/` directory.

## Key Dependencies

- `uv`: Python environment management and runner.
- `polars`: Data processing library.
- `httpx`: HTTP client for data fetching.

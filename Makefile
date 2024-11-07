.DEFAULT_GOAL := run

.PHONY: web run dev clean api

run:
	uv run dagster asset materialize --select \* -m datadex.definitions

dev:
	uv run dagster dev

setup:
	uv sync --all-extras --dev

web:
	python -m http.server -d web

api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

clean:
	rm -rf data/*.parquet data/*.duckdb

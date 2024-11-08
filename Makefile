.DEFAULT_GOAL := run

.PHONY: run dev setup web api space clean

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

space:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/datadex --delete '*' --repo-type=space "Dockerfile"

clean:
	rm -rf data/*.parquet data/*.duckdb

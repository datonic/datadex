.DEFAULT_GOAL := run
.PHONY: web run dev clean

run:
	uv run dagster asset materialize --select \* -m datadex.definitions

dev:
	uv run dagster dev

web:
	python -m http.server -d web

clean:
	rm -rf data/*.parquet data/*.duckdb

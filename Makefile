.DEFAULT_GOAL := run

run:
	uv run dagster-dbt project prepare-and-package --file datadex/dbt/resources.py
	uv run dagster asset materialize --select \* -m datadex.definitions

dev:
	uv run dagster dev

preview:
	quarto preview portal

setup:
	command -v uv >/dev/null 2>&1 || pip install -U uv
	uv sync
	. .venv/bin/activate

dbt-docs:
	. .venv/bin/activate; cd dbt; uv run dbt docs generate --profiles-dir .
	mkdir -p dbt/target/docs
	cp dbt/target/*.json dbt/target/index.html dbt/target/graph.gpickle dbt/target/docs/

render: dbt-docs
	quarto render portal
	cp -r dbt/target/docs/ portal/.quarto/output/dbt

clean:
	rm -rf data/*.parquet data/*.duckdb
	rm -rf dbt/target dbt/dbt_packages dbt/logs
	rm -rf portal/.quarto
	rm -rf .venv

.DEFAULT_GOAL := run

run:
	dagster asset materialize --select \* -m datadex

dev:
	dagster dev

preview:
	quarto preview portal

setup:
	@command -v uv >/dev/null 2>&1 || pip install -U uv
	uv venv
	uv pip install -U -e ".[dev]"
	. .venv/bin/activate

dbt-docs:
	cd dbt && dbt docs generate --profiles-dir .
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

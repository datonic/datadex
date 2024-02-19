.DEFAULT_GOAL := run

run:
	dagster job execute -j data_assets_job -m datadex

hf:
	dagster job execute -j hf_assets_job -m datadex

dev:
	dagster dev -m datadex

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

evidence:
	npm --prefix ./portal/reports install
	npm --prefix ./portal/reports run sources
	npm --prefix ./portal/reports run build

render: dbt-docs evidence
	cp README.md portal/README.md
	quarto render portal
	cd portal && quarto render README.md -M output-file:index
	cp -r dbt/target/docs/ portal/.quarto/output/dbt
	cp -r portal/reports/build/ portal/.quarto/output/reports
	rm portal/README.md

clean:
	rm -rf data/*.parquet data/*.duckdb
	rm -rf dbt/target dbt/dbt_packages dbt/logs
	rm -rf portal/.quarto

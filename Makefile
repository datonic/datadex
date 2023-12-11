.DEFAULT_GOAL := run

run:
	dagster asset materialize --select \* -m datadex.dag

dev:
	dagster dev -m datadex.dag

preview:
	quarto preview portal

dbt-docs:
	cd dbt && dbt docs generate --profiles-dir .
	mkdir -p dbt/target/docs
	cp dbt/target/*.json dbt/target/index.html dbt/target/graph.gpickle dbt/target/docs/

render: run dbt-docs
	cp README.md portal/README.md
	quarto render portal
	cd portal && quarto render README.md -M output-file:index
	cp -r dbt/target/docs/ portal/.quarto/output/dbt
	rm portal/README.md

clean:
	rm -rf data/*.parquet data/*.duckdb
	rm -rf dbt/target dbt/dbt_packages dbt/logs
	rm -rf portal/.quarto

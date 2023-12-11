.DEFAULT_GOAL := run

run:
	dagster asset materialize --select \* -m datadex.dag

dev:
	dagster dev -m datadex.dag

preview:
	quarto preview

docs:
	cd dbt && dbt docs generate --profiles-dir .
	mkdir -p dbt/target/docs
	cp dbt/target/*.json dbt/target/index.html dbt/target/graph.gpickle dbt/target/docs/

render: docs
	quarto render
	quarto render README.md -M output-file:index
	cp -r dbt/target/docs/ .quarto/output/docs

clean:
	rm -rf data/*.parquet data/*.duckdb
	rm -rf .quarto
	rm -rf dbt/target dbt/dbt_packages dbt/logs

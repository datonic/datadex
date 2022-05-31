deps:
	@dbt clean
	@dbt deps
	@dbt run-operation stage_external_sources

run:
	@dbt run

rill: run
	@mkdir -p ~/rill
	@rill init --project ~/rill --db target/local.db --copy
	@rill start --project ~/rill
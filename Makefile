deps:
	@dbt clean
	@dbt deps
	@dbt run-operation stage_external_sources

run: deps
	@dbt run

clean: deps
	@dbt clean

rill: run
	@mkdir -p ~/rill
	@rill init --project ~/rill --db target/local.db
	@rill start --project ~/rill
deps:
	@dbt clean
	@dbt deps
	@dbt run-operation stage_external_sources

run:
	@dbt run
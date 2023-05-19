.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.8.0

deps: clean
	@cd dbt && dbt deps

run: deps
	@cd dbt && dbt run

dagster:
	@dagster dev -m datadex.dagster

clean:
	@cd dbt && dbt clean
	@rm -rf data/* output .quarto

rill:
	@rill start ~/rill

evidence: run
	@npm --prefix ./reports install
	@npm --prefix ./reports run dev

build:
	docker build -t $(IMAGE_NAME) -t davidgasquez/datadex:latest .

push:
	docker push $(IMAGE_NAME)

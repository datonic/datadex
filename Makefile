.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.3.0

deps: clean
	@dbt deps
	@dbt run-operation stage_external_sources

run:
	@dbt run

clean:
	@dbt clean

rill: run
	@mkdir -p ~/rill
	@rill init --project ~/rill
	@rill start --project ~/rill

build:
	docker build -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

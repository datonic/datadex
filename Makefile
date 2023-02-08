.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.6.0

deps: clean
	@dbt deps

run:
	@dbt run

clean:
	@dbt clean

rill: run
	@rill start --project rill

build:
	docker build -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

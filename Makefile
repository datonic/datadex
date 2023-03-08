.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.7.0

deps: clean
	@dbt deps

run:
	@dbt run

clean:
	@dbt clean

alto.toml:
	@pip install singer-alto
	@alto init --no-prompt

data: alto.toml
	@alto tap-carbon-intensity:target-jsonl
.PHONY: get-data

rill: run
	@rill start --project rill

build:
	docker build --no-cache -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

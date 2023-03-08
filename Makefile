.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.7.0

deps: clean
	@dbt deps

run:
	@dbt run

clean:
	@dbt clean

# Set up alto
alto.toml:
	@pip install singer-alto
	@alto init --no-prompt

# Extract and load data to the devcontainer
data: alto.toml
	@rm -rf output ||:
	@alto tap-carbon-intensity:target-jsonl
.PHONY: data

# A complete ELT example
carbon-elt: data deps
	@dbt run -s +fct_carbon_intensity__index
.PHONY: carbon-elt

rill: run
	@rill start --project rill

build:
	docker build --no-cache -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

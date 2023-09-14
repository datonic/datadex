.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v1.0.0

deps: clean
	@dbt deps --project-dir dbt;

run: deps
	@dagster asset materialize --select \* -m datadex;

dev:
	@dagster dev -m datadex

docs:
	@dbt docs generate --project-dir dbt;
	@mkdir -p dbt/target/docs
	@cp dbt/target/*.json dbt/target/index.html dbt/target/graph.gpickle dbt/target/docs/

quarto: docs
	@quarto render
	@quarto render README.md -M output-file:index
	@cp -r dbt/target/docs/ .quarto/output/docs

preview:
	@quarto preview

clean:
	@dbt clean --project-dir dbt;
	@rm -rf data/* output .quarto target dbt_packages

rill:
	@curl -s https://cdn.rilldata.com/install.sh | bash
	@rill start ~/rill

build:
	docker build -t $(IMAGE_NAME) -t davidgasquez/datadex:latest .

push:
	docker push $(IMAGE_NAME)

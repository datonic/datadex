.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.8.0

deps: clean
	@dbt deps --project-dir dbt;

run: deps
	@dbt run --project-dir dbt;

dagster:
	@dagster dev -m datadex.dagster

docs:
	@dbt docs generate --project-dir dbt;
	@mkdir -p dbt/target/docs
	@cp target/*.json target/index.html target/graph.gpickle dbt/target/docs/

quarto:
	@quarto render
	@quarto render README.md -M output-file:index
	@cp -r dbt/target/docs/ .quarto/output/docs

preview:
	@quarto preview

clean:
	@dbt clean --project-dir dbt;
	@rm -rf data/* output .quarto target

rill:
	@rill start ~/rill

evidence:
	@npm --prefix ./reports install;
	@npm --prefix ./reports run dev;

build:
	docker build -t $(IMAGE_NAME) -t davidgasquez/datadex:latest .

push:
	docker push $(IMAGE_NAME)

.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.8.0

deps: clean
	@cd dbt && dbt deps

run: deps
	@dagster asset materialize -m datadex --select "*"

clean:
	@cd dbt && dbt clean

rill:
	@rill start --project ~/rill

evidence: run
	@npm --prefix ./reports install
	@npm --prefix ./reports run dev

build:
	docker build -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v0.7.1

deps: clean
	@dbt deps

run: deps
	@dbt run

clean:
	@git clean -fdx

rill:
	@rill start --project rill

evidence: run
	@npm --prefix ./reports install
	@npm --prefix ./reports run dev

build:
	docker build --no-cache -t $(IMAGE_NAME) .

push:
	docker push $(IMAGE_NAME)

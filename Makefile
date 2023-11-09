.DEFAULT_GOAL := run

IMAGE_NAME := davidgasquez/datadex:v1.0.0

run:
	@dagster asset materialize --select \* -m datadex.dag;

dev:
	@dagster dev -m datadex.dag

docs:
	@dbt docs generate --project-dir dbt --profiles-dir dbt;
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

docker-run:
	docker run -it --rm -u vscode -e DAGIT_HOST=0.0.0.0 -p 3000:3000 \
		-v $(PWD):/workspaces/datadex \
		--env-file .env \
		$(IMAGE_NAME) /bin/bash

push:
	docker push $(IMAGE_NAME)

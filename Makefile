.DEFAULT_GOAL := run

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

.PHONY: dev
dev:
	uv run dg dev


.PHONY: run
run:
	uv run dg launch --assets '*'

web:
	npm install --prefix web
	npm run dev --prefix web

api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

space:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/datadex --delete '*' --repo-type=space "Dockerfile"

clean:
	rm -rf data/*.parquet data/*.duckdb

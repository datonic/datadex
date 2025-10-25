.DEFAULT_GOAL := data

HF_COMMAND := uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} --repo-type dataset

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

data: .uv data/wdi/world_development_indicators.parquet data/owid/owid_indicators.parquet

data/wdi/world_development_indicators.parquet: datasets/wdi.py
	@echo "[run] wdi"
	@uv run datasets/wdi.py

data/owid/owid_indicators.parquet: datasets/owid.py
	@echo "[run] owid"
	@uv run datasets/owid.py

.PHONY: upload
upload: data
	$(HF_COMMAND) datonic/owid_indicators data/owid data
	$(HF_COMMAND) datonic/world_development_indicators data/wdi data

.PHONY: web
web:
	python -m http.server 8000 --directory web

.PHONY: api
api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

.PHONY: clean
clean:
	rm -rf data/wdi data/owid

.PHONY: lint
lint:
	uvx ruff check
	uvx ty check

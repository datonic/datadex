.DEFAULT_GOAL := data

PACKAGE_NAME := datadex

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

data: .uv data/world_development_indicators.parquet data/owid_indicators.parquet

data/world_development_indicators.parquet: $(PACKAGE_NAME)/wdi.py
	@echo "[run] wdi"
	@uv run $(PACKAGE_NAME)/wdi.py

data/owid_indicators.parquet: $(PACKAGE_NAME)/owid.py
	@echo "[run] owid"
	@uv run $(PACKAGE_NAME)/owid.py

upload: data/owid_indicators.parquet data/world_development_indicators.parquet
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/owid_indicators data/owid_indicators.parquet data/owid_indicators.parquet --repo-type dataset
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/world_development_indicators data/world_development_indicators.parquet data/world_development_indicators.parquet --repo-type dataset

.PHONY: web
web:
	python -m http.server 8000 --directory web

api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

clean:
	rm -rf data/*.parquet

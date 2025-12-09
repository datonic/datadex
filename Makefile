.DEFAULT_GOAL := data

HF_COMMAND := uv run hf upload --token=${HUGGINGFACE_TOKEN} --repo-type dataset

.PHONY: .uv
.uv:
	@uv --version >/dev/null || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

data: .uv datasets/world_development_indicators/data/world_development_indicators.parquet datasets/owid_indicators/data/owid_indicators.parquet

datasets/world_development_indicators/data/world_development_indicators.parquet: datasets/world_development_indicators/wdi.py
	@echo "[run] wdi"
	@uv run datasets/world_development_indicators/wdi.py

datasets/owid_indicators/data/owid_indicators.parquet: datasets/owid_indicators/owid.py
	@echo "[run] owid"
	@uv run datasets/owid_indicators/owid.py

.PHONY: upload
upload: data
	$(HF_COMMAND) datonic/owid_indicators datasets/owid_indicators
	$(HF_COMMAND) datonic/world_development_indicators datasets/world_development_indicators

.PHONY: web
web:
	python -m http.server 8000 --directory web

.PHONY: api
api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

.PHONY: clean
clean:
	rm -rf datasets/*/data

.PHONY: lint
lint:
	uvx ruff check
	uvx ty check

.DEFAULT_GOAL := data

DD := datadex
HF_COMMAND := uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} --repo-type dataset

.PHONY: .uv
.uv:
	@uv --version || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

data: .uv data/world_development_indicators/world_development_indicators.parquet data/owid_indicators/owid_indicators.parquet

data/world_development_indicators/world_development_indicators.parquet: $(DD)/wdi.py
	@echo "[run] wdi"
	@uv run $(DD)/wdi.py

data/owid_indicators/owid_indicators.parquet: $(DD)/owid.py
	@echo "[run] owid"
	@uv run $(DD)/owid.py

.PHONY: upload
upload: data
	$(HF_COMMAND) datonic/owid_indicators data/owid_indicators data
	$(HF_COMMAND) datonic/world_development_indicators data/world_development_indicators data

.PHONY: web
web:
	python -m http.server 8000 --directory web

.PHONY: api
api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

.PHONY: clean
clean:
	rm -rf data/world_development_indicators data/owid_indicators

.PHONY: lint
lint:
	uvx ruff check
	uvx ty check

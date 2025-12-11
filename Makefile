.DEFAULT_GOAL := data

PYTHON ?= uv run
HF_COMMAND := uv run hf upload --token=${HUGGINGFACE_TOKEN} --repo-type dataset

DATASET_SCRIPTS := $(sort $(wildcard datasets/*/*.py))
DATASET_DIRS := $(sort $(patsubst %/,%,$(dir $(DATASET_SCRIPTS))))
DATASET_NAMES := $(notdir $(DATASET_DIRS))

.PHONY: .uv
.uv:
	@uv --version >/dev/null || echo 'Please install uv: https://docs.astral.sh/uv/getting-started/installation/'

.PHONY: setup
setup: .uv
	uv sync --frozen

.PHONY: data
data: .uv
	@for script in $(DATASET_SCRIPTS); do \
		echo "[run] $$script"; \
		$(PYTHON) $$script; \
	done

.PHONY: upload
upload: data
	@for name in $(DATASET_NAMES); do \
		echo "[upload] $$name"; \
		$(HF_COMMAND) datonic/$$name datasets/$$name; \
	done

.PHONY: web
web:
	python -m http.server 8000 --directory web

.PHONY: api
api:
	uv run huggingface-cli upload --token=${HUGGINGFACE_TOKEN} datonic/api --repo-type=space --delete "*" ./api .

.PHONY: clean
clean:
	rm -rf $(addsuffix /data,$(DATASET_DIRS))

.PHONY: lint
lint:
	uvx ruff check
	uvx ty check

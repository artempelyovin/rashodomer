REPO_DIR ?= $(shell git rev-parse --show-toplevel)

format:
	uv run ruff format $(REPO_DIR)/src
	uv run ruff check $(REPO_DIR)/src --select I --fix
#include .env
#export

.PHONY : install format test

## Development
install:
	uv sync

format:
	uv run ruff format --exclude '*.ipynb' .
	uv run nbqa ruff amazon_reviews_dataset.ipynb


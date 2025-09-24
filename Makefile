#include .env
#export

.PHONY : install format test

## Development
install:
	uv sync

format:
	uv run ruff format .

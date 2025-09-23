include .env
export

.PHONY : install format test

## Development
install:
	uv sync

format:
	ruff format .

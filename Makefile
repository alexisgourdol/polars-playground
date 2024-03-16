include .env
export

.PHONY : install format test

## Development
install:
	poetry install

format:
	ruff format .

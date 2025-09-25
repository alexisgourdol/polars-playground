# Project Name

Polars playground

## Description

Goal : get familiar with polars, docs and features


## Features
- uses .devcontainers and runs notebook within VS Code (for standalone use of jupyterlab or jupyter notebooks, see uv integration considerations https://docs.astral.sh/uv/guides/integration/jupyter/)
- dependencies
    - polars, pyarrow (to use some functions of polars such as to_arrow, to_pandas ...)
    - ipykernel , pip to use notebooks within VS Code
    - ruff to format the code

Note 1 : if you need to exec into the docker container, remember to either use `uv run` to use the virtualenv, or activate it manually
- `python -c "import polars"` will fail
- `uv run python -c "import polars"` will succeed

Note 2 :
RUN apt update && apt install less -y


## Prerequisites
- docker
- VS Code
- optional for version control should this repo be cloned and turned into a larger project

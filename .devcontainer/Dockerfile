ARG PLATFORM=amd64
FROM --platform=linux/${PLATFORM} python:3.12

ENV UV_LINK_MODE=copy

RUN apt update && apt install less -y
RUN pip install uv --no-cache-dir


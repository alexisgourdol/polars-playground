ARG PLATFORM=amd64
FROM --platform=linux/${PLATFORM} python:3.12

RUN apt update && apt install less -y
RUN pip install uv --no-cache-dir

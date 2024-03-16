# Project Name

A Basic Template Dev Container for Data Analysis and Data Pipeline Project in Python with Duck DB

## Description

This repository provides a basic template for setting up a development container for data analysis and data pipeline projects using Python and Duck DB. The dev container is pre-configured with the necessary tools and dependencies to get started quickly.

Credits to :
- Mehdi Ouazza <mehdi@mehd.io> for the original repo https://github.com/mehd-io/pypi-duck-flow/
    - changes : removed project specifig configs and files
- Jeroen Overschie (@dunnkers)  https://github.com/godatadriven/python-devcontainer-template
    - changes : updated .gitignore and removed requirements.txt set up in Dockerfile in favour of Poetry in the devcontainer.json > `postCreateCommand`
    - TO DO : improve Dockerfile to run as non-root user (1st attempt failed to build container due to permission errors, so rolled back)
    - TO DO : set up portsAttributes and forwardPorts to add Streamlit as the go to data viz lib
    - TO DO : set up the CI/CD on github


## Features

- Docker-based development environment
- Python with Duck DB pre-installed
- Easy setup and configuration

## Prerequisites

Before getting started, make sure you have the following installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository:

    ```shell
    git clone https://github.com/your-username/your-repo.git
    ```

2. Change into the project directory:

    ```shell
    cd your-repo
    ```

3. Start the dev container:

    ```shell
    docker-compose up -d
    ```

4. Access the dev container:

    ```shell
    docker exec -it your-container-name bash
    ```

5. You're now inside the dev container and ready to start working on your data analysis and data pipeline project!

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


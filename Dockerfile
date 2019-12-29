from python:3.6.8

env POETRY_VERSION=1.0.0
env TENSORFLOW_VERSION=1.15

run pip install "tensorflow==$TENSORFLOW_VERSION"
run pip install "poetry==$POETRY_VERSION"
run poetry config virtualenvs.create false

copy pyproject.toml pyproject.toml
run poetry install --no-root

copy README.md README.md
copy storybro/ storybro/

run poetry install

volume /models

entrypoint storybro

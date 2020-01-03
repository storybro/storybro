from python:3.6.8

run apt-get update
run apt-get install -y git aria2 unzip

workdir /storybro

env POETRY_VIRTUALENVS_CREATE=false

run pip install poetry tensorflow==1.15

run touch README.md
copy pyproject.toml pyproject.toml

run sed -i '/tensorflow/d' pyproject.toml

run poetry install --no-root

copy storybro/ storybro/

run pip install .

volume /models

entrypoint ["storybro"]

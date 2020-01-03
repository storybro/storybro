from python:3.6.8

run apt-get update

workdir /storybro

copy ./bin/linux/install/python-version-check /bin/python-version-check
run python-version-check

copy ./bin/linux/install/install-system-packages /bin/install-system-packages
run install-system-packages

run pip install tensorflow==1.15

run touch README.md
copy pyproject.toml pyproject.toml

copy ./bin/linux/install/install-python-packages /bin/install-python-packages
run install-python-packages

copy storybro/ storybro/

copy ./bin/linux/install/install-storybro /bin/install-storybro
run install-storybro

volume /models

entrypoint ["storybro"]

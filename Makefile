# .DEFAULT_GOAL := local
# .PHONY: tests
SHELL := /bin/bash

# General Commands
help:
	cat Makefile

install:
	pipenv install

install_dev:
	pipenv install --dev

locked_dev:
	pipenv install --dev --ignore-pipfile

locked_install:
	pipenv install --ignore-pipfile

lock_pip_file:
	pipenv shell
	pipenv --python 3.9
	pipenv lock
	pipenv requirements > requirements.txt

requirements:
	pipenv run pip freeze > requirements.txt

init:
	pipenv install -r requirements.txt 

install_tools:
	bash scripts/install_dev_tools.sh

clean: clean_rm

clean_rm:
	pipenv --rm

fresh: clean_rm install

# Automated Testing
test:
	pipenv run pytest tests --junitxml=report.xml

# Development Commands
lint:
	pipenv run prospector

types:
	pipenv run mypy .

coverage:
	pipenv run coverage run -m unittest discover tests;
	pipenv run coverage report

format:
	pipenv run yapf -i *.py **/*.py **/**/*.py

format_check:
	pipenv run yapf --diff *.py **/*.py **/**/*.py

pycodestyle:
	pycodestyle

qa: lint types tests format_check pycodestyle

# Application Specific Commands
run:
	# pipenv run cd src && streamlit run json.py
	pipenv run streamlit run src/main.py

SHELL := /bin/bash

test:
	pytest --cov=src tests/

build:
	python tmp.py

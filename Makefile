SHELL := /bin/bash

init:
	poetry init

install:
	poetry install
	# poetry install --no-root (no dev)

test:
	python -m unittest discover -s ./tests -p '*_test.py'

.PHONY: test

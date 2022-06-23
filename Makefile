SHELL := /bin/bash

init:
	poetry init

install:
	poetry install
	# poetry install --no-root (no dev)

.PHONY: test
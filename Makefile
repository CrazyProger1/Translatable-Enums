.PHONY: test
test:
	poetry run python -m pytest tests/

.PHONY: build
build:
	poetry build

.PHONY: help
help:
	poetry run python -m i18n -h

.PHONY: coverage
coverage:
	poetry run coverage run -m pytest


.PHONY: coverage-report
coverage-report: coverage;
	poetry run coverage report -m


.PHONY: format
format:
	poetry run python -m black tests
	poetry run python -m black i18n

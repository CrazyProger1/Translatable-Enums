
.PHONY: test
test:
	poetry run python -m pytest tests/


.PHONY: build
build:
	poetry build


.PHONY: help
help:
	poetry run python -m i18n -h
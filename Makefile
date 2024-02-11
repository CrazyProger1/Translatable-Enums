
.PHONY: test
test:
	poetry run python -m pytest tests/


.PHONY: build
build:
	poetry build
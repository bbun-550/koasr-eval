.PHONY: setup lint test smoke check clean

UV ?= uv

setup:
	$(UV) python install 3.12
	$(UV) sync --all-extras --dev --locked

lint:
	$(UV) run ruff check .

test:
	$(UV) run pytest

smoke:
	$(UV) run koasr-eval --help

check: lint test smoke

clean:
	rm -rf .pytest_cache .ruff_cache build dist

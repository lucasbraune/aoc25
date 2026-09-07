PY = python3.14
VENV = .venv
PYTHON = $(VENV)/bin/python
DEPS = $(VENV)/.deps
CODE = src test
CACHES = .pytest_cache .ruff_cache

.PHONY: test part1 part2 check fix format clean

test: $(DEPS)
	$(PYTHON) -m pytest

part1: $(PYTHON)
	$(PYTHON) src/part1.py

part2: $(PYTHON)
	$(PYTHON) src/part2.py

check: $(DEPS)
	@fail=0; \
	$(PYTHON) -m ruff check || fail=1; \
	$(VENV)/bin/pyright || fail=1; \
	exit $$fail

fix: $(DEPS)
	$(PYTHON) -m ruff check --fix

format: $(DEPS)
	$(PYTHON) -m ruff format

clean:
	rm -rf $(CACHES)
	find $(CODE) -type d -name __pycache__ -prune -exec rm -rf {} +
	rm -rf $(VENV)

# The venv itself.
$(PYTHON):
	$(PY) -m venv $(VENV)

# Dev deps; re-runs when pyproject.toml changes.
$(DEPS): pyproject.toml | $(PYTHON)
	$(PYTHON) -m pip install --group dev
	touch $@

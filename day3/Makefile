PY = python3.14
VENV = .venv
PYTHON = $(VENV)/bin/python
DEPS = $(VENV)/.deps

.PHONY: test part1 format clean

test: $(DEPS)
	$(PYTHON) -m pytest

part1: $(PYTHON)
	$(PYTHON) src/part1.py

part2: $(PYTHON)
	$(PYTHON) src/part2.py

format: $(DEPS)
	$(PYTHON) -m ruff format

clean:
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf $(VENV)
	rm -rf src/__pycache__
	rm -rf test/__pycache__

# The venv itself.
$(PYTHON):
	$(PY) -m venv $(VENV)

# Dev deps; re-runs when pyproject.toml changes.
$(DEPS): pyproject.toml | $(PYTHON)
	$(PYTHON) -m pip install --group dev
	touch $@

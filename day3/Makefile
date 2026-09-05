PY = python3.14
VENV = .venv
PYTHON = $(VENV)/bin/python
DEPS = $(VENV)/.deps

.PHONY: test part1 format

test: $(DEPS)
	$(PYTHON) -m pytest

part1: $(PYTHON)
	$(PYTHON) src/part1.py

format: $(DEPS)
	$(PYTHON) -m ruff format

# The venv itself.
$(PYTHON):
	$(PY) -m venv $(VENV)

# Dev deps; re-runs when pyproject.toml changes.
$(DEPS): pyproject.toml | $(PYTHON)
	$(PYTHON) -m pip install --group dev
	touch $@

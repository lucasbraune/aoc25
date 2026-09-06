PY = python3.14
VENV = .venv
PYTHON = $(VENV)/bin/python
DEPS = $(VENV)/.deps
CODE = src test
CACHES = .pytest_cache .ruff_cache

.PHONY: test part1 part2 lint format clean distclean

test: $(DEPS)
	$(PYTHON) -m pytest

part1: $(PYTHON)
	$(PYTHON) src/part1.py

part2: $(PYTHON)
	$(PYTHON) src/part2.py

lint: $(DEPS)
	$(PYTHON) -m ruff check

format: $(DEPS)
	$(PYTHON) -m ruff format

# Caches and bytecode. Keeps the venv, so the next build is fast.
clean:
	rm -rf $(CACHES)
	find $(CODE) -type d -name __pycache__ -prune -exec rm -rf {} +

# Everything clean does, plus the venv. Next `make` reinstalls from scratch.
distclean: clean
	rm -rf $(VENV)

# The venv itself.
$(PYTHON):
	$(PY) -m venv $(VENV)

# Dev deps; re-runs when pyproject.toml changes.
$(DEPS): pyproject.toml | $(PYTHON)
	$(PYTHON) -m pip install --group dev
	touch $@

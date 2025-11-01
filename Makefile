#***************************************************************************************
# * File: Makefile
# * Author: Vatsal Gupta
# * Date: 21-Sep-2025
# * Description: Makefile for managing the application.
# **************************************************************************************/

#***************************************************************************************
# * License
# **************************************************************************************/
# This file is licensed under the Apache 2.0 License.
# License information should be updated as necessary.

#***************************************************************************************
# * Variables
# **************************************************************************************/
SRC_DIR := src

#***************************************************************************************
# * Targets
# **************************************************************************************/
.PHONY: all run test clean

all: clean sync run

sync:
	@uv sync --no-cache
freeze: sync
	@uv export --quiet --no-header --no-annotate --no-hashes --format requirements.txt --output-file requirements.txt
run: sync
	@uv run --directory $(SRC_DIR) streamlit run app.py --browser.gatherUsageStats false
test: sync
	@echo "No tests available currently."
# 	@uv test
clean:
	@rm -rf __pycache__ .pytest_cache .mypy_cache .venv
	@uv clean

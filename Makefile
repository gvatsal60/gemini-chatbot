# Makefile for managing project tasks

SRC_DIR := src

all:
	uv sync
run:
	@uv run --directory $(SRC_DIR) streamlit run app.py --browser.gatherUsageStats false
clean:
	uv clean

.PHONY: all clean
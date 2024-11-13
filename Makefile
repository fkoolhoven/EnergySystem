SRC_DIR = src
TEST_DIR = test

install:
	pip install -r requirements.txt
	pip install -e .

run:
	python -m src.app

test:
	pytest -v

format:
	ruff format $(SRC_DIR) $(TEST_DIR)
	ruff check --fix --select I,E,W,F,N,RUF,TRY,UP,W $(SRC_DIR) $(TEST_DIR)

.PHONY: install run test format
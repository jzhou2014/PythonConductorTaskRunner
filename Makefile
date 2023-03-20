dev: 
	python3 src/main.py
uvicorn:
	PYTHONPATH=.:./src uvicorn src.main:app --reload
test:
	PYTHONPATH=.:./src pytest -v
test-ci:
	PYTHONPATH=.:./src pytest --ignore="src/tests/integration" -v --cov=src --cov-report=xml --junitxml=report.xml

fastapi:
	uvicorn src.main:app --reload

format:
	black src/

install:
	pip install -r requirements.txt

lint:
	flake8 src/

freeze:
	pip freeze > requirements.txt

build:
	docker-compose build --no-cache

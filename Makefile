    
run:
	python -m service

migrate:
	alembic upgrade --heads

test:
	py.test tests

check:
	flake8

black-check:
	black --check .

format:
	black .

coverage:
	pytest --cov=service tests/ & coverage html

    
run:
	@python -m service

migrate:
	@alembic upgrade --heads

test:
	py.test tests

check:
	flake8

format:
	black .

coverage:
	pytest --cov=service tests/units & coverage html

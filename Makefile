create-env:
	python3 -m venv dev-env

activate-env:
	conda activate fastapi-crud

deactivate-env:
	conda deactivate

install-requirements:
	pip install -r requirements.txt

add-requirements:
	pip freeze > requirements.txt

run:
	uvicorn src.main:app --reload

create-container:
	docker run -d --name fastapi-crud -p 8000:8000 fastapi-simple-api

build:
	docker-compose --build -d

build-up:
	docker-compose up

build-down:
	docker-compose down

migrate:
	alembic revision --autogenerate -m "Migration name"
	alembic upgrade head

migrate-rollback:
	alembic downgrade base
	alembic updgrade head

check-migration:
	alembic current
# Atalhos para o dia a dia. Rode, por exemplo: make up
# Atenção: as linhas de comando começam com TAB, não com espaços.
# Os alvos test e lint serão acrescentados quando existir o projeto Python.

.PHONY: up down logs psql

up:
	docker compose up -d --wait

down:
	docker compose down

logs:
	docker compose logs -f db

psql:
	docker compose exec db sh -c 'psql -U "$$POSTGRES_USER" -d "$$POSTGRES_DB"'

.PHONY: test lint

test:
	uv run pytest

lint:
	uv run ruff check . && uv run ruff format --check . && uv run mypy
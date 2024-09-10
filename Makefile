#!/usr/bin/env python3

install:
	poetry install

lock:
	poetry lock

up-prod:
	poetry run python3 manage.py migrate
	poetry run gunicorn task_manager.wsgi -b 0.0.0.0:4000

up-dev:
	poetry run python3 manage.py migrate
	poetry run python3 manage.py runserver 0.0.0.0:7000

migrations:
	poetry run python3 manage.py makemigrations --name $(name)

migrate:
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

test-coverage:
	poetry run coverage run --source='.' manage.py test task_manager
	poetry run coverage report -m
	poetry run coveralls

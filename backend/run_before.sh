#!/bin/sh
echo "Start RUN_BEFORE"
pipenv run python run_before.py
pipenv run python manage.py collectstatic --noinput
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
# pipenv run python manage.py collectstatic --noinput
echo "End RUN_BEFORE"
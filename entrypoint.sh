#!/usr/bin/env bash

cd /app

python manage.py db upgrade

python manage.py runserver --port 5000 --threaded

#!/usr/bin/env bash

cd /app

python manage.py db init

python manage.py runserver --threaded

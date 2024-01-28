#!/bin/bash

python /app/init_mongo.py

celery -A celery_app worker --loglevel=info &
celery -A celery_app beat --loglevel=info &

python /app/test.py
python /app/main.py

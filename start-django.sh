#!/bin/bash
python manage.py collectstatic --no-input
python manage.py migrate

if [[ "$ENV_STATE" == "production"]]; then
  gunicorn djproject.wsgi --workers 2 $GUNICORN_WORKERS --forwarded-allow-ips "*"
else
  python manage.py runserver 0.0.0.0:8000
fi

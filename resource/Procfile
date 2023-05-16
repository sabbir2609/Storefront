release: python manage.py migrate
web: gunicorn core.wsgi
worker: celery -A core worker
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')

celery = Celery('storefront')
celery.config_from_object('django.conf:settings', namespace='CELERY')

celery.autodiscover_tasks()

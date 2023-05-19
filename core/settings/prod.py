import os

from .common import *
from .common import BASE_DIR

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = [os.environ['DJANGO_HOST']] if 'DJANGO_HOST' in os.environ else []

CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['DJANGO_HOST']] if 'DJANGO_HOST' in os.environ else []

DEBUG = False

# Database settings
conn_str = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
conn_str_params = {pair.split('=')[0]: pair.split('=')[1] for pair in conn_str.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': conn_str_params['dbname'],
        'HOST': conn_str_params['host'],
        'USER': conn_str_params['user'],
        'PASSWORD': conn_str_params['password'],
    }
}


# cache settings
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
REDIS_URL = os.environ['REDIS_URL']

# redis://username:password@host:port/db
CELERY_BROKER_URL = f'redis://default:{REDIS_PASSWORD}@{REDIS_URL}'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": f"redis://default@{REDIS_URL}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD,
        }
    }
}

# email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ["SMTP_SERVER"]
EMAIL_HOST_USER = os.environ["SMTP_LOGIN"]
EMAIL_HOST_PASSWORD = os.environ["SMTP_PASSWORD"]
EMAIL_PORT = os.environ["SMTP_PORT"]

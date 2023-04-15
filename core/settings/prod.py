import os
from .common import *
# import dj_database_url

DEBUG = False

# SECRET_KEY = os.environ['SECRET_KEY']

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-$&ovi=euv((gdjh1xbuck7ou3rzj1xa*xa%zn6sindeh70gmbp')

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else ['storefrontx.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

# Configure Postgres database; the full username for PostgreSQL flexible server is 
# username (not @sever-name). 

hostname = os.environ['DBHOST']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'PORT': '5432',
        'HOST': hostname + ".postgres.database.azure.com",
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASS'],
        "OPTIONS" : {"sslmode" : "require"}
    }
}

REDIS_URL = os.environ['REDIS_URL']
REDIS_USER = os.environ['REDIS_USER']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']

# redis://username:password@host:port/db
CELERY_BROKER_URL = f'redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_URL}'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": f"redis://{REDIS_USER}@{REDIS_URL}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD,
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['SMTP_SERVER']
EMAIL_HOST_USER = os.environ['SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['SMTP_PASSWORD']
EMAIL_PORT = os.environ['SMTP_PORT']

import os
from .common import *
# import dj_database_url

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['storefrontx.azurewebsites.net']

DATABASES = {
    'default': dj_database_url.config()
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['SMTP_SERVER']
EMAIL_HOST_USER = os.environ['SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['SMTP_PASSWORD']
EMAIL_PORT = os.environ['SMTP_PORT']

import os

from .common import *

SECRET_KEY = os.environ["SECRET_KEY"]

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

DEBUG = False

conn_str = os.environ["AZURE_POSTGRESQL_CONNECTIONSTRING"]
conn_str_params = {
    pair.split("=")[0]: pair.split("=")[1] for pair in conn_str.split(" ")
}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": conn_str_params["dbname"],
        "HOST": conn_str_params["host"],
        "USER": conn_str_params["user"],
        "PASSWORD": conn_str_params["password"],
        "OPTIONS": {"sslmode": conn_str_params["sslmode"]},
    }
}

# azure redis cache provides direct access to redis inside the azure network
AZURE_REDIS_CONNECTIONSTRING = os.environ["AZURE_REDIS_CONNECTIONSTRING"]

# REDIS_USER = os.environ["REDIS_USER"]
# REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]

# redis://username:password@host:port/db
# CELERY_BROKER_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_URL}"

# azure integrated cache
CELERY_BROKER_URL = os.environ["AZURE_REDIS_CONNECTIONSTRING"]

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": AZURE_REDIS_CONNECTIONSTRING,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SSL": True,
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ["SMTP_SERVER"]
EMAIL_HOST_USER = os.environ["SMTP_LOGIN"]
EMAIL_HOST_PASSWORD = os.environ["SMTP_PASSWORD"]
EMAIL_PORT = os.environ["SMTP_PORT"]

import os

from .common import *
from .common import BASE_DIR

# import dj_database_url

SECRET_KEY = os.environ["SECRET_KEY"]

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = (
    [os.environ["WEBSITE_HOSTNAME"]] if "WEBSITE_HOSTNAME" in os.environ else []
)
CSRF_TRUSTED_ORIGINS = (
    ["https://" + os.environ["WEBSITE_HOSTNAME"]]
    if "WEBSITE_HOSTNAME" in os.environ
    else []
)

DEBUG = False


# Configure Postgres database based on connection string of the libpq Keyword/Value form
# https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNSTRING
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
        "OPTIONS": {"sslmode": "require"},
    }
}

# azure redis cache provides direct access to redis inside the azure network
REDIS_URL = os.environ["REDIS_URL"]

# REDIS_USER = os.environ["REDIS_USER"]
# REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]

# redis://username:password@host:port/db
# CELERY_BROKER_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_URL}"

# azure integrated cache
CELERY_BROKER_URL = REDIS_URL

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": REDIS_URL,
        # probably not needed
        # "OPTIONS": {
        #     "CLIENT_CLASS": "django_redis.client.DefaultClient",
        #     "PASSWORD": REDIS_PASSWORD,
        # },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ["SMTP_SERVER"]
EMAIL_HOST_USER = os.environ["SMTP_LOGIN"]
EMAIL_HOST_PASSWORD = os.environ["SMTP_PASSWORD"]
EMAIL_PORT = os.environ["SMTP_PORT"]

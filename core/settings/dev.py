from .common import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

if DEBUG:
    MIDDLEWARE += ["silk.middleware.SilkyMiddleware"]

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "storefront",
#         "USER": "postgres",
#         "PASSWORD": "2609",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["AZURE_POSTGRESQL_NAME"],
        'USER': os.environ["AZURE_POSTGRESQL_USER"],
        'PASSWORD': os.environ["AZURE_POSTGRESQL_PASSWORD"],
        'HOST': os.environ["AZURE_POSTGRESQL_HOST"],
        'PORT': 5432 ,
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}

CELERY_BROKER_URL = "redis://localhost:6379"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": "redis://localhost:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp4dev"
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_PORT = 2525

DJANGO_DEBUG_TOOLBAR = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

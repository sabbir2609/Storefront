from datetime import timedelta
from pathlib import Path
import os
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

IS_HEROKU = "DYNO" in os.environ

SECRET_KEY = 'django-insecure-$&ovi=euv((gdjh1xbuck7ou3rzj1xa*xa%zn6sindeh70gmbp'

if 'SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ["SECRET_KEY"]

if not IS_HEROKU:
    DEBUG = True


if IS_HEROKU:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok.io']

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8001",
    "http://127.0.0.1:8001",

    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

INSTALLED_APPS = [

    # for admin theme
    'colorfield',
    'admin_interface',

    # pre-installed
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django REST Framework
    'rest_framework',
    # auth
    'djoser',

    # add debug toolbar
    "debug_toolbar",

    # 3rd party
    'django_filters',
    "corsheaders",
    'silk',

    # new apps
    'store',
    'tags',
    'likes',
    'main',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # debug-toolbar middleware
    "debug_toolbar.middleware.DebugToolbarMiddleware",

    # WhiteNoiseMiddleware
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

]

# if DEBUG:
#     MIDDLEWARE += ['silk.middleware.SilkyMiddleware']  # silk middleware

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

if IS_HEROKU:
    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'NAME': 'd4q9e2uqv8kt1a',
        #     'USER': 'hlukwukzbywnhv',
        #     'PASSWORD': '9284be841954166ffc920be7b2c4f43e6779810c18acad9d854ed87d15bb4f04',
        #     'HOST': 'ec2-54-208-104-27.compute-1.amazonaws.com',
        #     'PORT': '5432',
        # }

        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'storefront',
            'USER': 'postgres',
            'PASSWORD': '9959',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }

        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'NAME': 'd4q9e2uqv8kt1a',
        #     'USER': 'hlukwukzbywnhv',
        #     'PASSWORD': '9284be841954166ffc920be7b2c4f43e6779810c18acad9d854ed87d15bb4f04',
        #     'HOST': 'ec2-54-208-104-27.compute-1.amazonaws.com',
        #     'PORT': '5432',
        # }

        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': BASE_DIR / 'db.sqlite3',
        # }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = 'staticfiles/'
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
# Default primary key field type


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# disable decimal -> string for rest framework

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ]
}

AUTH_USER_MODEL = 'main.User'

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'main.serializer.UserCreateSerializer',
        'current_user': 'main.serializer.UserSerializer'
    }
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@sabbir.inc'

ADMINS = [
    ('Mosh', 'admin@moshbuy.com')
]

CELERY_BROKER_URL = 'redis://localhost:6379/1'

# command -> celery -A core beat
CELERY_BEAT_SCHEDULE = {
    'notify_customers': {
        'task': 'home.tasks.notify_customers',
        'schedule': 5,  # crontab(day_of_week=1, hour=7, minute=30)
        'args': ['Hello World']
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

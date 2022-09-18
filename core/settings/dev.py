from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-$&ovi=euv((gdjh1xbuck7ou3rzj1xa*xa%zn6sindeh70gmbp'

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

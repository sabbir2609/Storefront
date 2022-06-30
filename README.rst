create a conda environment for the project
__________
conda create --name storefront-env

activate the conda environment
__________
source activate storefront-env

install the project dependencies
__________
pip install django

start the project
__________
dajngo-admin startproject core .

install django-debug-toolbar
__________ 
| pip install django-debug-toolbar 
| More :: `https://django-debug-toolbar.readthedocs.io/en/latest/`

Install psycopg2 to connect Postgres
__________
pip install psycopg2

Databse config for Postgres
__________
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'storefront',
        'USER': 'postgres',
        'PASSWORD': '2609',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

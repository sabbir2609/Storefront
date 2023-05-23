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
| DATABASES = {
|    'default': {
|        'ENGINE': 'django.db.backends.postgresql',
|        'NAME': 'storefront',
|        'USER': 'postgres',
|       'PASSWORD': '2609',
|        'HOST': '127.0.0.1',
|        'PORT': '5432',
|    }
| }

__________
| problem
duplicate key value violates unique constraint "store_product_pkey"
DETAIL:  Key (id)=(17) already exists.
| Solve
BEGIN;
SELECT setval(pg_get_serial_sequence('"store_product"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "store_product";
COMMIT;
# create a conda environment for the project
__________
conda create --name storefront-env

# activate the conda environment
__________
source activate storefront-env

# install the project dependencies
__________
pip install django

# start the project
__________
dajngo-admin startproject core .

# install django-debug-toolbar
__________ 
pip install django-debug-toolbar `Link [https://django-debug-toolbar.readthedocs.io/en/latest/]_`


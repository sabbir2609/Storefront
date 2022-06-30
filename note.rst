# create a conda environment for the project
conda create --name storefront-env

# activate the conda environment
source activate storefront-env

# install the project dependencies
pip install django

# start the project
dajngo-admin startproject core .


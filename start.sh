#!/bin/bash

# start postgresql
sudo service postgresql start

# start redis server
sudo service redis-server start

# activate virtual environment
source /home/sabbir/Storefront/venv/bin/activate

# start Django development server
python manage.py runserver

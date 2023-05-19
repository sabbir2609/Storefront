import os

from django.core.wsgi import get_wsgi_application

# Check for the DJANGO_HOST environment variable to see if we are running in Azure App Service
# If so, then load the settings from prod.py

settings_module = 'core.settings.prod' if 'DJANGO_HOST' in os.environ else 'core.settings.dev'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()

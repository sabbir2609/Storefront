import os

from django.core.wsgi import get_wsgi_application

# Check for the WEBSITE_HOSTNAME environment variable to see if we are running in Azure App Service
# If so, then load the settings from prod.py
# settings_module = 'core.settings.prod' if 'WEBSITE_HOSTNAME' in os.environ else 'core.settings.dev'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", core.settings.prod)

application = get_wsgi_application()

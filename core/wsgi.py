import os

from django.core.wsgi import get_wsgi_application

# Check for the WEBSITE_HOSTNAME environment variable to see if we are running in Azure App Service
# If so, then load the settings from prod.py
print('Inside core.wsgi')
print('WEBSITE_HOSTNAME' in os.environ)

settings_module = 'core.settings.prod' if 'WEBSITE_HOSTNAME' in os.environ else 'core.settings.dev'
print('settings_module', settings_module)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
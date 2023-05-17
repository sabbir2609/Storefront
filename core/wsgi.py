import os

from django.core.wsgi import get_wsgi_application

settings_module = "core.settings.prod" if "WEBSITE_HOSTNAME" in os.environ else "core.settings.dev"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()

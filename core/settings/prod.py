import os

from .common import *

# import dj_database_url

SECRET_KEY = os.environ["SECRET_KEY"]

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = (
    [os.environ["WEBSITE_HOSTNAME"]] if "WEBSITE_HOSTNAME" in os.environ else []
)
CSRF_TRUSTED_ORIGINS = (
    ["https://" + os.environ["WEBSITE_HOSTNAME"]]
    if "WEBSITE_HOSTNAME" in os.environ
    else []
)

DEBUG = False

# security.W004: This warning suggests that you should set the SECURE_HSTS_SECONDS setting to enable HTTP Strict Transport Security (HSTS) on your site. HSTS is a security feature that forces web browsers to always use HTTPS when communicating with your site, which can help protect against certain types of attacks.
SECURE_HSTS_SECONDS = 31536000  # 1 year

# security.W008: This warning suggests that you should set the SECURE_SSL_REDIRECT setting to True if your site should only be accessed over HTTPS. This setting will redirect any non-HTTPS requests to HTTPS, which can help prevent attackers from intercepting sensitive information.
SECURE_SSL_REDIRECT = True


# security.W012: This warning suggests that you should set the SESSION_COOKIE_SECURE setting to True to ensure that session cookies are only sent over HTTPS connections. This can help prevent attackers from hijacking user sessions.
SESSION_COOKIE_SECURE = True

# security.W019: This warning suggests that you should set the X_FRAME_OPTIONS setting to 'DENY' to prevent your site from being embedded in a frame or iframe on another site. This can help prevent clickjacking attacks.
X_FRAME_OPTIONS = "DENY"


# Configure Postgres database; the full username for PostgreSQL flexible server is
# username (not @sever-name).

hostname = os.environ["DBHOST"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DBNAME"],
        "PORT": "5432",
        "HOST": hostname + ".postgres.database.azure.com",
        "USER": os.environ["DBUSER"],
        "PASSWORD": os.environ["DBPASS"],
        "OPTIONS": {"sslmode": "require"},
    }
}

REDIS_URL = os.environ["REDIS_URL"]
REDIS_USER = os.environ["REDIS_USER"]
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]

# redis://username:password@host:port/db
CELERY_BROKER_URL = f"redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_URL}"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": f"redis://{REDIS_USER}@{REDIS_URL}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PASSWORD,
        },
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ["SMTP_SERVER"]
EMAIL_HOST_USER = os.environ["SMTP_LOGIN"]
EMAIL_HOST_PASSWORD = os.environ["SMTP_PASSWORD"]
EMAIL_PORT = os.environ["SMTP_PORT"]

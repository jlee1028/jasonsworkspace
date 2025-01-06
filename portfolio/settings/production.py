from .base_settings import *
from utils.secret_manager import get_secret
import json


SECRET_KEY = get_secret('django-secret-key', 'us-west-2')

DEBUG = False

ALLOWED_HOSTS = ['.jasonsworkspace.dev']

db_credentials = json.loads(get_secret('jws_db_credentials', 'us-west-2'))
db_endpoint = db_credentials['db_endpoint']
db_user = db_credentials['db_user']
db_password = db_credentials['db_password']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jws_db',
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_endpoint,
        'PORT': '5432',
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/django/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}

STATIC_ROOT = "/var/www/jasonsworkspace.dev/static"

# Require HTTPS
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Set referrer policy
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Add content security policy
MIDDLEWARE += ["csp.middleware.CSPMiddleware"]

# Allow browser to load external links
# ! replace 'unsafe-inline' with nonce
CSP_STYLE_SRC = ["'self'", "cdn.jsdelivr.net", "code.jquery.com", "stackpath.bootstrapcdn.com", "'unsafe-inline'"]

# Allow browser to load external scripts
CSP_SCRIPT_SRC = ["'self'", "cdn.jsdelivr.net", "code.jquery.com"]

# Allow browser to load external images
CSP_IMG_SRC = ["'self'", "data:"]

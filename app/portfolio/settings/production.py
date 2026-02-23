from .base_settings import *

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['.jasonsworkspace.dev']

# Databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/data/db.sqlite3",
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["console"]},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
    },
    "formatters": {
        "app": {
            "format": (
                "%(asctime)s [%(levelname)-8s] "
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

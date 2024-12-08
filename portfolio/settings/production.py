from .base_settings import *
from utils.secret_manager import get_secret


SECRET_KEY = get_secret('django-secret-key', 'us-west-2')

DEBUG = False

ALLOWED_HOSTS = ['.jasonsworkspace.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_ROOT = "/var/www/jasonsworkspace.com/static"

# Require HTTPS
SECURE_HSTS_SECONDS = 30 #2_592_000  # 30 days
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

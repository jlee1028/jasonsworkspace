from .base_settings import *
from utils.secret_manager import get_secret
import json

SECRET_KEY = get_secret('django-secret-key', 'us-west-2')
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

db_credentials = json.loads(get_secret('jws_db_credentials', 'us-west-2'))
db_endpoint = db_credentials['db_endpoint']
dev_user = db_credentials['dev_user']
dev_password = db_credentials['dev_password']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jws_db_dev',
        'USER': dev_user,
        'PASSWORD': dev_password,
        'HOST': db_endpoint,
        'PORT': '5432',
    }
}
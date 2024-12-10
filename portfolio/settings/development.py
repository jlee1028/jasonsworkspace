
from .base_settings import *

SECRET_KEY = 'abc123'
DEBUG = True
ALLOWED_HOSTS = ['.jasonsworkspace.dev', 'localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jws_db_dev',
        'USER': 'jason',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
import os

if os.environ['DJANGO_SETTINGS_MODULE'] == 'portfolio.settings.development':
   from .development import *
else:
   from .production import *
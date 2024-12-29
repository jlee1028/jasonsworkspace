import os

if os.environ['DJANGO_SETTINGS_MODULE'] == 'portfolio.settings.local_development':
   from .local_development import *
elif os.environ['DJANGO_SETTINGS_MODULE'] == 'portfolio.settings.development':
   from .development import *
else:
   from .production import *
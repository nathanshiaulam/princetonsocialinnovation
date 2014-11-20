from common import *
from os import environ

import dj_database_url
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = environ.get('DJANGO_SECRET_KEY', '')
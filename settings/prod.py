from common import *
from os import environ

import dj_database_url
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = environ.get('DJANGO_SECRET_KEY', '')

AWS_STORAGE_BUCKET_NAME = "princetonsocialinnovation"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MEDIA_URL = "https://%s.s3.amazonaws.com/" % os.environ['AWS_STORAGE_BUCKET_NAME']
MEDIA_ROOT = ''
AWS_ACCESS_KEY_ID = "nlam"
AWS_SECRET_ACCESS_KEY = "w8tfkhgby"
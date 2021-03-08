import os
from project_name.settings.production import *

TMP_PATH = os.path.abspath(os.path.join(BASE_DIR, 'tmp'))

DEBUG = True
SECRET = '42'

INTERNAL_IPS = ('127.0.0.1',)

if 'debug_toolbar' not in INSTALLED_APPS:
    INSTALLED_APPS += ('debug_toolbar',)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
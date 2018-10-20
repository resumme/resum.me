from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'testsecretkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    }
}

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.db',
    }
}

#  Required to serve the files while we use Gunicorn in dev env
MIDDLEWARE += [
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

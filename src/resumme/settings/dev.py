from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_URL = os.path.join(VUE_APP_DIR, 'public/')
STATIC_ROOT = None

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

#  Required to serve the files while we use Gunicorn in dev env
MIDDLEWARE += [
  'whitenoise.middleware.WhiteNoiseMiddleware',
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '/bundles/',  # must end with slash
        'STATS_FILE': os.path.join(VUE_APP_DIR, 'webpack-stats.json'),
    }
}

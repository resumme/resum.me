from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Only use the dev statics
STATIC_URL = '/dashboard/public/'
STATIC_ROOT = None
STATICFILES_DIRS = (
    os.path.join(VUE_APP_DIR, 'public'),
)

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

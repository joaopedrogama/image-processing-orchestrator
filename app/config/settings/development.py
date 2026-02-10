from config.settings.main import *

DEBUG = True


# HTTPS

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True


# Applications

TOP_PRIORITY_APPS += [
    'whitenoise.runserver_nostatic',
]

# Email

EMAIL_USE_WHITELIST = False

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

EMAIL_FILE_PATH = os.getenv('EMAIL_FILE_PATH', BASE_DIR / 'mails')


# Static and media files

SERVE_MEDIA = True

SERVE_STATIC = True

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}

_security_middleware_index = MIDDLEWARE.index('django.middleware.security.SecurityMiddleware')
MIDDLEWARE = [
    *MIDDLEWARE[: _security_middleware_index + 1],
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE[_security_middleware_index + 1 :],
]

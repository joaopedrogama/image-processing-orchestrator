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

MINIO_PUBLIC_BUCKETS = ["microservices-bucket"]
MINIO_PRIVATE_BUCKETS = []
MINIO_ENDPOINT="minio:9000"
MINIO_ACCESS_KEY="minioadmin"
MINIO_SECRET_KEY="minioadmin"
MINIO_USE_HTTPS=False
MINIO_REGION="us-east-1"

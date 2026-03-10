from config.settings.main import *

DEBUG = True


# HTTPS

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True

MINIO_PUBLIC_BUCKETS = ["microservices-bucket"]
MINIO_PRIVATE_BUCKETS = []

# storages.py
from django_minio_backend.models import MinioBackend
from django.conf import settings


def get_public_storage():
    if "microservices-bucket" not in settings.MINIO_PUBLIC_BUCKETS:
        raise ValueError("Bucket 'microservices-bucket' is not configured in MINIO_PUBLIC_BUCKETS.")
    return MinioBackend(
        bucket_name="microservices-bucket",
        storage_name="default",
    )

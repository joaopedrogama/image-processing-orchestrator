import re

from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from .api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]

if settings.SERVE_MEDIA:
    urlpatterns += [
        re_path(
            r"^{}(?P<path>.*)$".format(re.escape(settings.MEDIA_URL.lstrip("/"))),
            serve,
            kwargs={"document_root": settings.MEDIA_ROOT},
        ),
    ]

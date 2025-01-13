from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls")),
    path("drf/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns.extend(
        [
            path(
                "swagger/",
                SpectacularSwaggerView.as_view(url_name="schema"),
                name="swagger-ui",
            ),
            path("swagger/schema/", SpectacularAPIView.as_view(), name="schema"),
            path(
                "swagger/redoc/",
                SpectacularRedocView.as_view(url_name="schema"),
                name="redoc",
            ),
        ]
    )

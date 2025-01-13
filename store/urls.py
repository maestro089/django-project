from django.urls import path
from rest_framework.routers import DefaultRouter

from store.views import CategoryViewSet, CategoryModelViewSet

router = DefaultRouter()

router.register(r"category", CategoryViewSet, basename="category")
router.register(r"category-model", CategoryModelViewSet, basename="category-model")

urlpatterns = router.urls

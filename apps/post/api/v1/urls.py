from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.post.api.v1.viewsets import PostViewSet

router = DefaultRouter()

router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path("", include(router.urls)),
]

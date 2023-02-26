from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"", views.MovieViewSet, basename="movie")
router.register(r"genres", views.GenreViewSet, basename="genre")

urlpatterns = [path("", include(router.urls))]

from django.shortcuts import render
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre

from rest_framework.response import Response

# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

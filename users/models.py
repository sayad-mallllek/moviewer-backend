from django.db import models
from moviewer.utils import SoftDeleteModel


class Users(SoftDeleteModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    watched_movies = models.ManyToManyField(
        "movies.Movie", related_name="watched_users"
    )

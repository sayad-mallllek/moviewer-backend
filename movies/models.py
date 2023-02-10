from django.core.validators import MaxValueValidator, MinValueValidator
from moviewer.utils import SoftDeleteModel
from django.db import models


class Genre(SoftDeleteModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Movie(SoftDeleteModel):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=100)
    plot = models.TextField()
    poster = models.URLField()
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
    )
    runtime = models.IntegerField()

    def __str__(self):
        return self.title

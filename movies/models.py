from django.core.validators import MaxValueValidator, MinValueValidator
from moviewer.utils import SoftDeleteModel
from django.db import models


class InitialMovieDump(SoftDeleteModel):
    has_been_dumped = models.BooleanField(default=False)


class Genre(SoftDeleteModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MovieDisplayTimes(SoftDeleteModel):
    display_time = models.DateTimeField()
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)


# Create your models here.
class Movie(SoftDeleteModel):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    director = models.CharField(max_length=100)
    plot = models.TextField()
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        default=0.0,
    )
    runtime = models.DurationField()
    rental_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    purchase_price = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title

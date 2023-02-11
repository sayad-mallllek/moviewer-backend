from rest_framework import serializers

from .models import Movie, Genre, MovieDisplayTimes


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "title",
            "year",
            "director",
            "rating",
            "genres",
            "runtime",
            "plot",
            "rental_price",
            "purchase_price",
            # "display_times",
        )

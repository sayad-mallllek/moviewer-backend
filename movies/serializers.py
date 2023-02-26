from rest_framework import serializers

from .models import Movie, Genre


class MovieSerializer(serializers.ModelSerializer):

    display_times = serializers.SerializerMethodField()

    def get_display_times(self, obj):
        return [dt.display_time for dt in obj.moviedisplaytimes_set.all()]

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "year",
            "director",
            "rating",
            "genres",
            "runtime",
            "plot",
            "rental_price",
            "purchase_price",
            "display_times",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")

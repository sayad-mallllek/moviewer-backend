from rest_framework import serializers

from .models import Movie, Genre, MovieDisplayTimes


class MovieSerializer(serializers.ModelSerializer):

    display_times = serializers.SerializerMethodField()

    def get_display_times(self, obj):
        return [dt.display_time for dt in obj.moviedisplaytimes_set.all()]

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
            "display_times",
        )

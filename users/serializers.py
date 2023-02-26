from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    watched_movies = serializers.SerializerMethodField()

    def get_watched_movies(self, obj):
        return [movie for movie in obj.watched_movies.all()]

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
        )

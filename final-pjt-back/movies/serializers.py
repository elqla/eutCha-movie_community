from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Movie, Genre

User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    like_users = UserSerializer(read_only=True, many=True)
    dislike_users = UserSerializer(read_only=True, many=True)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movies = MovieSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = '__all__'

class ProfileMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
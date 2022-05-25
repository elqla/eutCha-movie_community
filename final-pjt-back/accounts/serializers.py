from rest_framework import serializers
from movies.models import Movie, Genre
from articles.models import Article
from django.contrib.auth import get_user_model



class ProfileSerializer(serializers.ModelSerializer):
    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = '__all__'
    articles = ArticleSerializer(read_only=True, many=True)


    class MovieSerializer(serializers.ModelSerializer):
        class GenreSerializer(serializers.ModelSerializer):
            class Meta:
                model = Genre
                fields = '__all__'

        genres = GenreSerializer(read_only=True, many=True)
        class Meta:
            model= Movie
            fields= '__all__'
    like_movies = MovieSerializer(read_only=True, many=True)
    dislike_movies = MovieSerializer(read_only=True, many=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'nickname', 'picture','like_movies', 'dislike_movies', 'articles',)
from django.db import models
from django.conf import settings

class Genre(models.Model):
    genre = models.CharField(max_length=10000)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    credits = models.CharField(max_length=1000)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_movies")
    genres = models.ManyToManyField(Genre, related_name="movie")   ###array[integer]
    release_date = models.CharField(max_length=100)
    popularity = models.FloatField()
    movie_id = models.IntegerField()
    poster_url = models.URLField(max_length=1000)


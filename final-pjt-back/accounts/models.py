from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie


class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True)
    watch_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)
from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from movies.models import Movie


class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True)
    picture = ProcessedImageField(
        blank=True,
        upload_to='profile/', 
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 60},
        default='../static/accounts/default_profile.jpg'
    )
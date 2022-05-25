from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .serializers import ProfileSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer

@api_view(['GET',])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)


# watch_movie도 봤다는걸 어떻게 할지.. 했나..


    # watch_movies = user.watch_movie
    # watch_movie = dict()
    # if watch_movies:
    #     for movie_id in watch_movie:
    #         movie = Movie.objects.get(pk=movie_id)
    #         # movie = get_object_or_404(Movie, pk=movie_id)
    #         serializer = MovieSerializer(movie, many=True)
    #         # watch_movie.update(serializer)
    #         watch_movie.add(Response(serializer.data))
    serializer = ProfileSerializer(user)
    return Response(serializer.data)



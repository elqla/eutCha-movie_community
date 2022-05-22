from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer
from .models import Movie


@api_view(['GET'])
def eutgorithm(request):
    like_movies = request.user.like_movies.all()
    print(like_movies)
    movies = Movie.objects.all()[:5]

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def popular(request):
    movies = Movie.objects.order_by('-popularity')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recent(request):
    movies = Movie.objects.order_by('-release_date')[:5]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def movie_new(request):
    if request.user.is_staff:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user.is_staff:
            serializer = MovieSerializer(instance=movie, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user.is_staff:
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

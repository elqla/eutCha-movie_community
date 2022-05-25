from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import MovieSerializer, ProfileMovieSerializer
from .models import Movie, Genre



def export_genre(user):
    genres = dict()
    dislike_movies = user.dislike_movies.all()
    like_movies = user.like_movies.all()
    for like_movie in like_movies:
        for genre in like_movie.genres.all():
            if genres.get(genre):
                genres[genre] += 1
            else:
                genres[genre] = 1
    for dislike_movie in dislike_movies:
        for genre in dislike_movie.genres.all():
            if genres.get(genre):
                genres[genre] -= 1
            else:
                genres[genre] = -1
    return genres


@api_view(['GET'])
def eutgorithm(request):
    algorithm = export_genre(request.user)
    if algorithm:
        most_like_genre = max(algorithm, key=algorithm.get).genre
        most_hate_genre = min(algorithm, key=algorithm.get).genre
    else:
        most_like_genre = '모험'
        most_hate_genre = '없음'
    if most_like_genre == most_hate_genre:
        most_hate_genre = '없음'
    movies = Movie.objects.filter(genres__genre=most_like_genre)\
        .exclude(genres__genre=most_hate_genre).order_by('-popularity')[:8]
    popular_movies = Movie.objects.order_by('-popularity')[:5]
    if len(movies) < 8:
        serializer = MovieSerializer(popular_movies, many=True)
    else:
        serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

# 내가 좋아하는 장르 싫어하는 장르 하나씩 나오도록
@api_view(['GET'])
def eutgorithm_genre(request):
    algorithm = export_genre(request.user)
    if algorithm:
        most_like_genre = max(algorithm, key=algorithm.get).genre
        most_hate_genre = min(algorithm, key=algorithm.get).genre
    else:
        most_like_genre = '모험'
        most_hate_genre = '없음'
    if most_like_genre == most_hate_genre:
        most_hate_genre = '없음'
    return Response({ 
        'like_genre': most_like_genre,
        'dislike_genre': most_hate_genre,
    })


@api_view(['GET'])
def popular(request):
    movies = Movie.objects.order_by('-popularity')[:8]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recent(request):
    movies = Movie.objects.order_by('-release_date')[:8]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movies(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def movie_new(request):
    data = request.data
    genres = []
    for genreId in request.data['genres']:
        genre = get_object_or_404(Genre, pk=genreId)
        genres.append({ 'id': genre.pk, 'genre': genre.genre})
    data['genres'] = genres
    data['popularity'] = float(data['popularity'])
    data['movie_id'] = int(data['movie_id'])
    if request.user.is_staff:
        serializer = MovieSerializer(data=data)
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


@api_view(['POST'])
def like_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def dislike_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if movie.dislike_users.filter(pk=request.user.pk).exists():
        movie.dislike_users.remove(request.user)
    else:
        movie.dislike_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
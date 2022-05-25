from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer, CommunitySerializer
from .models import Article, Comment
from movies.models import Movie
from django.db.models import Count
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def article_list(request):
    def article_list():
        articles = Article.objects.order_by('-pk')
        # articles = get_list_or_404(Article)[::-1]
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    if request.method == 'GET':
        return article_list()


@api_view(['POST'])
def article_create(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    if request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie = movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    def article_detail():
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    def article_update():
        if article.user == request.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data)
    def article_delete():
        if article.user == request.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            ## 삭제 메세지는 vue에서 구현

    if request.method == 'GET':
        return article_detail()
    elif request.method == 'PUT':
        return article_update()
    elif request.method == 'DELETE':
        return article_delete()


@api_view(['POST'])
def comment_create(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=user)
        # 사용자가 입력한 comment도 추가
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def comment_update():
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)
    def comment_delete():
        if request.user==comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

    if request.method=='PUT':
        comment_update()
    elif request.method=='DELETE':
        comment_delete()


# @api_view(['GET'])
# def community(request):
#     community = Article.objects.annotate(
#             comment_count=Count('comments', distinct=True)
#         ).order_by('-pk')
#     serializer = CommunitySerializer(community, many=True)
#     return Response(serializer.data)


@api_view(['GET'])
def community(request, page):
    community = Article.objects.annotate(
            comment_count=Count('comments', distinct=True)
        ).order_by('-pk')#[5*(page-1):5*page]
    serializer = CommunitySerializer(community, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profile_articles(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    articles = get_list_or_404(Article, user=user)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_articles(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    articles = get_list_or_404(Article, movie=movie)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

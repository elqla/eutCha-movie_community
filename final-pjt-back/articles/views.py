from django.shortcuts import get_list_or_404, get_object_or_404, render
from .serializers import ArticleSerializer, CommentSerializer, ArticleListSerializer
from .models import Article, Comment
from django.db.models import Count

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from articles import serializers


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
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


@api_view(['GET'])
def article_list(request):
    articles = Article.objects.order_by('-pk')
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)



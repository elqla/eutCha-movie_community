from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Article, Comment

User =  get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname',)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        exclude = ('updated_at', )  #('pk', 'user', 'content', 'article',)   ### created_at안써줘도 vue에서 접근 가능한가 ?
        read_only_fields = ('article',)



class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname',)
            
    # queryset annotate (views에서 채워줄것!)
    user = UserSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = '__all__'
        

# class ArticleListSerializer(serializers.ModelSerializer):
#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = ('nickname',)
            
#     # queryset annotate (views에서 채워줄것!)
#     user = UserSerializer(read_only=True)
#     comment = CommentSerializer(read_only=True, many=True)
#     class Meta:
#         model = Article
#         fields = '__all__'


class CommunitySerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('nickname',)
    user = UserSerializer(read_only=True)
    comment_count = serializers.IntegerField()
    # watch_movie = User.watch_movie
    class Meta:
        model = Article
        exclude = ('updated_at',)

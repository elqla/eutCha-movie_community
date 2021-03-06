from django.urls import path
from . import views
# 'api/v1/articles/'


app_name="articles"
urlpatterns = [
    # articles
    path('', views.article_list),
    path('new/<int:movie_pk>/', views.article_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    path('profile/<str:username>/', views.profile_articles), 
    path('movies/<int:movie_pk>/', views.movie_articles),
    # comments
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # community
    path('community/<int:page>/', views.community),
]
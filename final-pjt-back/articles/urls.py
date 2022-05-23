from django.urls import path
from . import views
# 'api/v1/articles/'


app_name="articles"
urlpatterns = [
    # articles
    path('', views.article_list_or_create),
    path('<int:article_pk>/', views.article_detail_or_update_or_delete),
    # comments
    path('<int:article_pk>/comments/', views.comment_create),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    # community
    path('community/<int:page>/', views.community),

]
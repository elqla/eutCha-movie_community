from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    path('eut/', views.eutgorithm),
    path('popular/', views.popular),
    path('recent/', views.recent),
    path('new/', views.movie_new),
    path('<int:movie_pk>/', views.movie_detail),
]
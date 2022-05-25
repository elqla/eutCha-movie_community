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
    serializer = ProfileSerializer(user)
    return Response(serializer.data)



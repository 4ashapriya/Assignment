from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from person.models import Profile
from person.serializers import UserCreationSerializer


class UserCreationAPI(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserCreationSerializer


class UserUpdateAPI(APIView):
    def post(self, request, *args, **kwargs):
        user = Profile.objects.get(id=request.data.get('id'))
        user.hobbies= request.data.get('hobbies')
        user.fav_movies = request.data.get('fav_movies')
        user.save()
        return Response({'status': 'success'})




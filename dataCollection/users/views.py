from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, ExtraInfoSerializer
from .models import ExtraInfo
# Create your views here.
from django.contrib.auth import get_user_model

class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Hello Choreo!"})


class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    #queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ExtraInfoAdd(generics.ListCreateAPIView):
    queryset = ExtraInfo.objects.all()
    serializer_class = ExtraInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ExtraInfo.objects.filter(user=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)

class ExtraInfoDelete(generics.DestroyAPIView):
    serializer_class = ExtraInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user()
        return ExtraInfo.objects.filter(user=user)

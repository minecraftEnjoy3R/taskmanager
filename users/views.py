from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserSerializer
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


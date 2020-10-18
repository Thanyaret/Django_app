from django.shortcuts import render
from .models import maid, UserProfile, statusmaid, historymaid
from rest_framework import viewsets
from .serializers import UserProfileserializer, maidserializer, statusmaidserializer, historymaidserializer


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileserializer

class maidViewSet(viewsets.ModelViewSet):
    queryset = maid.objects.all()
    serializer_class = maidserializer

class statusmaidViewSet(viewsets.ModelViewSet):
    queryset = statusmaid.objects.all()
    serializer_class = statusmaidserializer

class historymaidViewSet(viewsets.ModelViewSet):
    queryset = historymaid.objects.all()
    serializer_class = historymaidserializer


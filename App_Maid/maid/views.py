from django.shortcuts import render
from .models import maid, User, statusmaid, historymaid
from rest_framework import viewsets
from .serializers import userserializer, maidserializer, statusmaidserializer, historymaidserializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer

class maidViewSet(viewsets.ModelViewSet):
    queryset = maid.objects.all()
    serializer_class = maidserializer

class statusmaidViewSet(viewsets.ModelViewSet):
    queryset = statusmaid.objects.all()
    serializer_class = statusmaidserializer

class historymaidViewSet(viewsets.ModelViewSet):
    queryset = historymaid.objects.all()
    serializer_class = historymaidserializer


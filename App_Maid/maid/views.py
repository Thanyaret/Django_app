from django.shortcuts import render
from .models import maid,User
from rest_framework import viewsets
from .serializers import userserializer,maidserializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer

class maidViewSet(viewsets.ModelViewSet):
    queryset = maid.objects.all()
    serializer_class = maidserializer
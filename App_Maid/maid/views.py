from django.shortcuts import render
from .models import maid, UserProfile, statusmaid, historymaid
from rest_framework import viewsets
from .serializers import UserProfileserializer, maidserializer, statusmaidserializer, historymaidserializer,CustomUserDetailSerializer,UserSerializer
from rest_auth.registration.views import RegisterView
from rest_auth.views import UserDetailsView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class UserProfileViewSet(UserDetailsView):
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        user_profile = user.userprofile
        print("user",user_profile)
        user_profile_data = {
            "pk" : user.pk,
            "username" : user.username,
            "f_name"  : user.first_name
        }
        # try :
        #     user_profile_data['photo'] =  user_profile.photo 
        # except ValueError  as e :
        #     user_profile_data['photo'] =  None 
 
        return Response(user_profile_data)

class maidViewSet(viewsets.ModelViewSet):
    queryset = maid.objects.all()
    serializer_class = maidserializer

class statusmaidViewSet(viewsets.ModelViewSet):
    queryset = statusmaid.objects.all()
    serializer_class = statusmaidserializer

class historymaidViewSet(viewsets.ModelViewSet):
    queryset = historymaid.objects.all()
    serializer_class = historymaidserializer


from .models import UserProfile, maid, statusmaid,historymaid,User
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        fields  = "__all__"
        model = User
class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CustomUserDetailSerializer(UserDetailsSerializer):
    profile = UserProfileserializer(read_only=True)
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile',)

class maidserializer (serializers.ModelSerializer):
    class Meta:
        model = maid
        fields = [ 'id',
                    'photo',
                   'name',
                   'age',
                   'phone',
                   'detail',
                   'date',
                   'skill',
                   'review'
        ]

class statusmaidserializer(serializers.ModelSerializer):
    maid_name = maidserializer(read_only=True)
    class Meta:
        model = statusmaid
        fields = [
                  'id',
                  'maid_name',
                  'status'
                  ]


class historymaidserializer(serializers.ModelSerializer):
    class Meta:
        model = historymaid
        fields = [
                  'id',
                  'maid'
                  ]


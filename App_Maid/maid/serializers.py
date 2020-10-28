from .models import UserProfile, maid, statusmaid,historymaid,User
from rest_framework import serializers
from rest_auth.serializers import UserDetailsSerializer


class UserProfileserializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileserializer(read_only=True)
    class Meta : 
        fields  = "__all__"
        model = User

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
                   'skill',
                   'review'
        ]

class statusmaidserializer(serializers.ModelSerializer):
    maid_name_data = maidserializer(source='maid_name',read_only=True)
    class Meta:
        model = statusmaid
        fields = [
                  'id',
                  'maid_name',
                  'maid_name_data',
                  'date',
                  'user',
                  'status'
                  ]
    # def create (self,validated_data):
    #     booking = dict()
    #     booking["name"] = validated_data.get("name")
    #     booking["age"] = validated_data.get("age")
    #     booking["Phone"] = validated_data.


class historymaidserializer(serializers.ModelSerializer):
    maid_history_data = maidserializer(source='maid_history', read_only=True)
    class Meta:
        model = historymaid
        fields = [
                  'id',
                    'maid_history',
                    'user',
                    'maid_history_data',
                  ]


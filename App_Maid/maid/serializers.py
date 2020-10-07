from .models import User,maid
from rest_framework import serializers


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'id',
                    'photo',
                   'name',
                   'phone',
                   'username',
                   'password',
                   'address'
        ]

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

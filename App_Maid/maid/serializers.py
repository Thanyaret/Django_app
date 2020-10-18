from .models import User, maid, statusmaid,historymaid
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

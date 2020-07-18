from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    pass
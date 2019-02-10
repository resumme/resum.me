from django.contrib.auth.models import User
from core.models import Bio
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class BioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bio

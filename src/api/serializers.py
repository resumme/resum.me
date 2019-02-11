from django.contrib.auth.models import User
from core.models import Bio, CourseStatus, Course, ProviderProfile
from rest_framework import serializers
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class BioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bio
        exclude = ('user',)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'url')


class ProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        exclude = ()


class CousesStatusSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    profile = ProviderProfileSerializer()

    class Meta:
        model = CourseStatus
        # fields = ('course',)
        exclude = ('id',)

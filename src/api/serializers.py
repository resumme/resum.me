from django.contrib.auth.models import User
from core.models import Bio, CourseStatus, Course, ProviderProfile
from rest_framework import serializers
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class BioSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Bio
        fields = ('user', 'first_name', 'last_name', 'mail', 'description', 'resume', 'birth_date', 'avatar')


class BioRestrictedSerializer(BioSerializer):
    class Meta:
        model = Bio
        fields = ('bio',)


class CourseSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    provider = serializers.StringRelatedField()


    class Meta:
        model = Course
        fields = ('title', 'url', 'badge', 'provider', 'tags',)


class ProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        exclude = ()


class CousesStatusSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CourseStatus
        fields = ('course', 'status')

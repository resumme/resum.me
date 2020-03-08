from django.contrib.auth.models import User
from core.models import UserProfile, CourseStatus, Course, ProviderProfile, TimelineItem
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class BioSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('user', 'first_name', 'last_name', 'mail', 'resume', 'birth_date', 'avatar')


class BioRestrictedSerializer(BioSerializer):
    """
    This is used to avoid the update of some fields in this model
    """
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'mail', 'resume', 'birth_date', 'avatar')


class CourseSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    provider = serializers.StringRelatedField()


    class Meta:
        model = Course
        fields = ('title', 'url', 'badge', 'provider', 'tags',)


class ProviderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderProfile
        fields = ('error', 'username_provider')


class TimelineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimelineItem
        fields = ('title', 'description', 'type', 'start_date', 'end_date')


class CousesStatusSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = CourseStatus
        fields = ('course', 'completed')

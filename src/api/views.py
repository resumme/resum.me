from django.shortcuts import get_object_or_404

from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from core.models import UserProfile, CourseStatus, ProviderProfile, TimelineItem

from .serializers import (BioSerializer, CousesStatusSerializer,
                          BioRestrictedSerializer, ProviderProfileSerializer,
                          TimelineItemSerializer)

from .mixins import PublicApiViewPermissionsMixin, NoPaginateMixin


class UserCoursesListApi(PublicApiViewPermissionsMixin, ListAPIView):
    """
    This endpoint is public. Login is not required to use this path.

    This endpoint allows you to view your courses. Response is paginated
    """
    queryset = CourseStatus.objects.all()
    serializer_class = CousesStatusSerializer

    def get_queryset(self):
        return self.queryset.filter(profile__user__username=self.kwargs['username'])


class UserCoursesAllListApi(UserCoursesListApi, NoPaginateMixin):
    """
    This endpoint is public. Login is not required to use this path.

    This endpoint allows you to get all courses in a batch
    """


class TimelineListApi(PublicApiViewPermissionsMixin, ListAPIView):
    """
    This endpoint is public. Login is not required to use this path.

    This endpoint allows you to view your courses. Response is paginated
    """
    queryset = TimelineItem.objects.all()
    serializer_class = TimelineItemSerializer

    def get_queryset(self):
        return self.queryset.filter(user__username=self.kwargs['username'])


class TimelineAllListApi(TimelineListApi, NoPaginateMixin):
    """
    This endpoint is public. Login is not required to use this path.

    This endpoint allows you to get all courses in a batch
    """


class UserDataListUpdateView(RetrieveUpdateAPIView):
    """
    User must be logged to manage his data.

    This endpoint allows you to view and modify your user profile data.
    """
    queryset = UserProfile.objects.all()
    serializer_class = BioSerializer

    def put(self, request, *args, **kwargs):
        self.serializer_class = BioRestrictedSerializer
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        self.serializer_class = BioRestrictedSerializer
        return self.partial_update(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class UserProviderProfileRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    User must be logged to manage his data.

    This endpoint allows you to view and modify one of
    your provider profile data.
    """
    queryset = ProviderProfile.objects.all()
    serializer_class = ProviderProfileSerializer

    def get_queryset(self):
        provider = self.kwargs['provider']
        return self.queryset.filter(user=self.request.user, provider__name=provider)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class UserProviderProfileListView(ListAPIView):
    """
    User must be logged to manage his data.

    This endpoint allows you to view all your provider profiles.
    """
    queryset = ProviderProfile.objects.all()
    serializer_class = ProviderProfileSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

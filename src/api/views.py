from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView
from core.models import UserProfile, CourseStatus

from .serializers import UserSerializer, BioSerializer, CousesStatusSerializer, BioRestrictedSerializer

from .mixins import PublicApiViewPermissionsMixin


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bios to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = BioSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class UserCoursesView(ListAPIView):
    """
    User must be logged to manage his data.

    This endpoint allows you to view your courses.
    """
    queryset = CourseStatus.objects.all()
    serializer_class = CousesStatusSerializer

    def get_queryset(self):
        return self.queryset.filter(profile__user=self.request.user)


class UserCoursesAllView(UserCoursesView):
    """
    User must be logged to manage his data.

    This endpoint allows you to get all the courses in a batch from a logged user.
    """
    pagination_class = None


class UserCoursesPublicView(PublicApiViewPermissionsMixin, ListAPIView):
    """
    This endpoint is public. Login is not required to use this path.

    This endpoint allows you to view your courses. Response is paginated
    """
    queryset = CourseStatus.objects.all()
    serializer_class = CousesStatusSerializer

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs['username']
        return self.queryset.filter(profile__user__username=username)


class UserCoursesAllPublicView(UserCoursesPublicView):
    """
    This endpoint is public. Login is not required to use this path.

    This endpoint allows you to get all courses in a batch
    """
    pagination_class = None



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

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

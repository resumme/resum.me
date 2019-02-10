from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, BioSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows bios to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = BioSerializer

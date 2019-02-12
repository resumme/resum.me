from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from core.models import UserProfile, TimelineItem
from core.serializers import (serialize_profile, serialize_timeline_item, courses_from_username)


def profile_view(request, username):
    data = {}
    try:
        user = User.objects.get(username=username)
        data['profile'] = serialize_profile(
            UserProfile.objects.get(user=user)
        )

        data['timeline'] = [serialize_timeline_item(item) for item in TimelineItem.objects.filter(user=user).order_by('-start_date')]

        data['courses'] = courses_from_username(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'profiles/profile.html', data)

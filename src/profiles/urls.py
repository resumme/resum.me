from django.conf.urls import url
from profiles.views import profile_view

urlpatterns = [
    url(r'.*', profile_view),
]

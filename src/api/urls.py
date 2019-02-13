from api.views import UserCoursesPublicView, UserDataListUpdateView, UserCoursesView, UserCoursesAllPublicView, UserCoursesAllView
from django.conf.urls import url


urlpatterns = [
    url(r'^user/$', UserDataListUpdateView.as_view(), name='user_data'),
    url(r'^user/courses/$', UserCoursesView.as_view(), name='user_courses'),
    url(r'^user/courses/all/$', UserCoursesAllView.as_view(), name='user_courses_all'),
    url(r'^users/(?P<username>\w{0,50})/courses/$', UserCoursesPublicView.as_view(), name='user_courses_public'),
    url(r'^users/(?P<username>\w{0,50})/courses/all/$', UserCoursesAllPublicView.as_view(), name='user_courses_all_public'),
]

from django.urls import include, path
from rest_framework import routers
from api.views import UserViewSet, UsersViewSet, UserDataListUpdateView, UserCoursesView
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^user/$', UserDataListUpdateView.as_view(), name='user_data'),
    url(r'^user/courses/$', UserCoursesView.as_view(), name='user_sourses'),
]

from api.views import (UserCoursesListApi, UserDataListUpdateView,
                       UserCoursesAllListApi,
                       UserProviderProfileListView,
                       UserProviderProfileRetrieveUpdateAPIView, TimelineAllListApi, TimelineListApi)
from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Resum.me API",
      default_version='BETA 0.9',
      license=openapi.License(name="Made with ❤️ for the devs of the 🌎"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


"""
Public URLs:
   - r/api/user/<username>/courses/
   - r/api/user/<username>/courses/all/
   - r/api/user/<username>/timeline/
   - r/api/user/<username>/timeline/all/

Private URLs(User must be logged and provide a session code and CSRF token):
   - r/api/dashboard/user/
   - r/api/dashboard/user/providers/
   - r/api/dashboard/user/provider/<provider>/
"""

public_urls = [
    url(r'^user/(?P<username>\w{0,50})/courses/$',
        UserCoursesListApi.as_view(), name='user_courses_public'),
    url(r'^user/(?P<username>\w{0,50})/courses/all/$',
        UserCoursesAllListApi.as_view(), name='user_courses_all_public'),
    url(r'^user/(?P<username>\w{0,50})/timeline/$',
        TimelineListApi.as_view(), name='timeline_public'),
    url(r'^user/(?P<username>\w{0,50})/timeline/all/$',
        TimelineAllListApi.as_view(), name='timeline_all_public'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

auth_validated_urls = [
    url(r'^dashboard/user/$',
        UserDataListUpdateView.as_view(), name='user_data'),
    url(r'^dashboard/user/providers/$',
        UserProviderProfileListView.as_view(), name='user_providers'),
    url(r'^dashboard/user/provider/(?P<provider>\w{0,50})$',
        UserProviderProfileRetrieveUpdateAPIView.as_view())
]

urlpatterns = public_urls + auth_validated_urls

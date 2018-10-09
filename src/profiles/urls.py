
from django.conf.urls import url
from profiles.views import LoadProfileView, ProfileEditView, BioEditView

urlpatterns = [
    url(r'^edit/$', BioEditView.as_view(), name='profile_edit'),
    url(r'^providers/edit/(?P<pk>\d+)/$', ProfileEditView.as_view(), name='profile_provider_edit'),
    # url(r'^providers/edit/$', ProfileEditView.as_view(), name='profile_provider_edit'),
    url(r'.*', LoadProfileView),
]

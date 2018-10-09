from django.conf.urls import url
from dashboard.views import EditUserBioView, EditProviderProfileView, TimelineItemsListView, TimelineItemsCreateView, \
    TimelineItemDeleteView, TimelineItemUpdateView, ProviderListView

urlpatterns = [
    url(r'^$', EditUserBioView.as_view(), name='dashboard_home'),
    url(r'^provider-list/$', ProviderListView.as_view(), name='provider_list'),
    url(r'^timeline/add', TimelineItemsCreateView.as_view(), name='dashboard_timeline_add'),
    url(r'^timeline/edit/(?P<pk>\d+)/$', TimelineItemUpdateView.as_view(), name='dashboard_timeline_update'),
    url(r'^timeline/delete/(?P<pk>\d+)/$', TimelineItemDeleteView.as_view(), name='dashboard_timeline_delete'),
    url(r'^timeline/', TimelineItemsListView.as_view(), name='dashboard_timeline'),
    url(r'^(?P<pk>\w{0,50})/', EditProviderProfileView.as_view(), name='dashboard_edit_provider'),
]

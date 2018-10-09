from django.conf.urls import url
from django.contrib.auth import views as auth_views
from authentication import views as core_views

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]

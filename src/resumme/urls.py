"""resumme URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from landing.views import landing_page
from core.views import terms_and_condition, privacy
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^r/admin/', admin.site.urls),
    url(r'^r/dashboard/', include('dashboard.urls')),
    url(r'^r/auth/', include('authentication.urls')),

    # legal
    url(r'^r/privacy/', privacy, name='legal_privacy_policy'),
    url(r'^r/legal/', terms_and_condition, name='legal_terms'),

    #password reset
    url(r'^r/password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^r/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^r/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^r/reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^$', landing_page, name='landing'),

    url(r'^(?P<username>\w{0,50})/$', include('profiles.urls')),
]

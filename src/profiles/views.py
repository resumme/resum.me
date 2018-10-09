from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from django.views import View

from core.models import Bio, ProviderProfile, Provider, TimelineItem
from core.serializers import (serialize_user_provider_profiles,
                              serialize_profile, serialize_timeline_item, courses_from_username)
from django.views.generic import UpdateView, FormView, ListView
from django.urls import reverse_lazy
from profiles.forms import ProfileEditForm, BioEditForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin


def LoadProfileView(request, username):
    data = {}
    try:
        user = User.objects.get(username=username)
        data['profile'] = serialize_profile(
            Bio.objects.get(user=user)
        )

        data['timeline'] = [serialize_timeline_item(item) for item in TimelineItem.objects.filter(user=user).order_by('-start_date')]

        data['courses'] = courses_from_username(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'profiles/profile.html', data)


class BioEditView(LoginRequiredMixin, UpdateView):
    # form_class = ProfileEditForm
    form_class = BioEditForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('profile_edit')
    template_name = 'dashboard/edit_profile_form.html'

    def get_object(self):
        return self.request.user.bio

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['provider_profile_list'] = ProviderProfile.objects.filter(user=self.request.user)
        # ctx['providers'] = Provider.objects.filter()
        return ctx


class ProfileEditView(LoginRequiredMixin, UpdateView):
    # form_class = ProfileEditForm
    model = ProviderProfile
    form_class = ProfileEditForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('profile_edit')
    template_name = 'dashboard/edit_profile_form.html'

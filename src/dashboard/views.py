from django.http import Http404

from core.models import ProviderProfile, Provider, TimelineItem
from django.views.generic import UpdateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from dashboard.forms import EditUserBioForm, ProviderProfileEditForm, CreateTimelineItem
from django.contrib.auth.mixins import LoginRequiredMixin
from core.serializers import (serialize_user_provider_profiles,
                              serialize_profile, serialize_timeline_item)
from core.models import Bio, TimelineItem
from django.contrib.auth.models import User

from dashboard.mixins import CustomValidation
from django.http import HttpResponseRedirect


class GenericView(LoginRequiredMixin):
    model = TimelineItem
    form_class = CreateTimelineItem
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('dashboard_timeline')
    template_name = 'dashboard/timeline_add.html'

    def form_valid(self, form):
        candidate = form.save(commit=False)
        candidate.user = User.objects.get(username=self.request.user)  # use your own profile here
        candidate.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # ctx['provider_profile_list'] = ProviderProfile.objects.filter(user=self.request.user)

        # Obtain profile stats. FIXME: I explode if a do not have courses
        try:
            user = User.objects.get(username=self.request.user)
            data['username'] = user.username

            user_provider_profiles = user.providerprofile_set.all()
            provider_profile_nicknames = {}
            for profile in user_provider_profiles:
                provider_profile_nicknames[profile.provider.name] = profile.username_provider

            data['provider_profile_nicknames'] = provider_profile_nicknames

            data['profile'] = serialize_profile(
                Bio.objects.get(user=user)
            )

            data['timeline'] = [serialize_timeline_item(item) for item in
                                TimelineItem.objects.filter(user=user).order_by('-start_date')]

            data['courses'] = serialize_user_provider_profiles(
                ProviderProfile.objects.filter(user=user)
            )
            total_courses = len(data['courses']['completed']) + len(data['courses']['in_progress'])

            data['stats'] = {'total_courses': total_courses,
                             'courses_in_progress': len(data['courses']['in_progress']),
                             'courses_completed': len(data['courses']['completed'])}

        except Exception:
            pass
        data['providers'] = ProviderProfile.objects.filter(user=user,  provider__enabled=True)
        return data


class EditUserBioView(GenericView, UpdateView):
    form_class = EditUserBioForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('dashboard_home')
    template_name = 'dashboard/dashboard.html'

    def get_object(self):
        return self.request.user.bio


class ProviderListView(GenericView, ListView):
    template_name = 'dashboard/provider_list.html'

    def get_object(self):
        return self.request.user.bio

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['providers'] = ProviderProfile.objects.filter(user=self.request.user, provider__enabled=True)
        return ctx


class EditProviderProfileView(GenericView, UpdateView, CustomValidation):
    model = ProviderProfile
    form_class = ProviderProfileEditForm
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('provider_list')
    template_name = 'dashboard/edit_profile_form.html'

    def get_form_kwargs(self):
        self.validate_user(self.request.user, self.kwargs['pk'])
        return super().get_form_kwargs()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['providers'] = ProviderProfile.objects.filter(user=self.request.user, provider__enabled=True).exclude(pk=self.kwargs['pk'])
        ctx['main_provider'] = ProviderProfile.objects.get(pk=self.kwargs['pk'])
        return ctx


class TimelineItemsListView(GenericView, ListView):
    model = TimelineItem
    template_name = 'dashboard/timeline.html'
    context_object_name = 'timeline_items'

    def get_queryset(self):
        user = User.objects.get(username=self.request.user)
        return user.timelineitem_set.all()


class TimelineItemsCreateView(GenericView, CreateView):
    pass


class TimelineItemUpdateView(GenericView, UpdateView):
    pass


class TimelineItemDeleteView(DeleteView):
    model = TimelineItem
    success_url = reverse_lazy('dashboard_timeline')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise Http404

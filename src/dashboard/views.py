from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('dashboard')
    template_name = 'dashboard/dashboard.html'

from django.http import Http404

from core.models import ProviderProfile


class CustomValidation():
    def validate_user(self, user, profile):
        if not ProviderProfile.objects.filter(pk=profile, user=user).exists():
            raise Http404("Nop")

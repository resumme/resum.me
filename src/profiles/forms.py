# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from core.models import ProviderProfile, UserProfile


class BioEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ('username_provider',)

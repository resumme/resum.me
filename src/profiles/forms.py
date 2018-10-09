# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User
from django.forms import inlineformset_factory

from core.models import ProviderProfile, Bio


class BioEditForm(forms.ModelForm):
    class Meta:
        model = Bio
        exclude = ('user',)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ()


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ('username_provider',)

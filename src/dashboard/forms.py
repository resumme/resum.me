from core.models import Bio, ProviderProfile, TimelineItem
from django import forms


class EditUserBioForm(forms.ModelForm):
    class Meta:
        model = Bio
        exclude = ('user', 'bio', 'mail', 'birth_date')
        widgets = {
          'resume': forms.Textarea(attrs={'rows': 60, 'cols': 60, 'class': 'textarea'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditUserBioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name is 'resume':
                field.widget.attrs['class'] = 'textarea is-primary-focus'
            elif field_name is 'avatar':
                continue
            else:
                field.widget.attrs['class'] = 'input is-medium is-primary-focus'


class CreateTimelineItem(forms.ModelForm):
    class Meta:
        model = TimelineItem
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(CreateTimelineItem, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input is-medium is-primary-focus'
            if 'date' in field_name:
                field.widget.attrs['data-toggle'] = 'datepicker'



class ProviderProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProviderProfile
        fields = ('username_provider',)

    def __init__(self, *args, **kwargs):
        super(ProviderProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input is-medium'

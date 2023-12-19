from django import forms
from .models import Date, Entry
from django.core.exceptions import ValidationError


class DateForm(forms.ModelForm):
    class Meta:
        model = Date
        fields = ['title']
        widgets = {
            'title': forms.DateInput(attrs={'type': 'date'})
        }


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'description', 'priority', 'start_time', 'end_time']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 40}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if end_time <= start_time:
                raise ValidationError("End time should be greater than start time.")

        return cleaned_data


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['image']


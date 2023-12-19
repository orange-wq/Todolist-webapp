from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']

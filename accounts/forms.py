from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile



class CustomUserCreationForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('telephone',)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class SignUpForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','is_staff']


from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=200)
    lastname = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ["username", "firstname", "lastname", "email", "password1", "password2"]


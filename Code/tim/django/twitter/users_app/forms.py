from unittest.util import _MAX_LENGTH
from django import forms

# create form


class NewSignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', max_length=10)
    first_name = forms.CharField(label='First Name', max_length=20)
    last_name = forms.CharField(label='Last Name', max_length=20)
    email = forms.CharField(label='email', max_length=20)


class NewLoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label="password", max_length=10)

from django import forms
from django.forms import ModelForm
from .models import *

class NewTweetForm(forms.Form):
    text = forms.CharField(label='Tweet', max_length=120)
    
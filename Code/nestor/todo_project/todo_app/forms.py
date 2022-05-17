from django import forms
from django.forms import ModelForm
from .models import *

class NewItem(forms.Form):
    item = forms.CharField(label='item', max_length=120)
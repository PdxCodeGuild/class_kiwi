from email.policy import default
from django import forms
from django.forms import ModelForm
from .models import *


class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = ("completed",)

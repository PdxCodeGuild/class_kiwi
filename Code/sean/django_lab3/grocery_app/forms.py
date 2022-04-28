from dataclasses import fields
from django import forms
from django.forms import ModelForm
from . models import *


class GroceryForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = '__all__'

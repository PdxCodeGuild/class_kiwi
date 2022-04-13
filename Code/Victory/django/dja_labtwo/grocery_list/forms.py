from django import forms
from django.forms import ModelForm
from .models import *

class GroceryForm(forms.ModelForm):
    title=forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add New task'}))

    class Meta:
        model = Grocery
        fields = '__all__'
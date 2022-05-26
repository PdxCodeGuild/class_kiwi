from django import forms
from django.forms import ModelForm
from .models import *


class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'enter task'})
        }
        fields = '__all__'


class PriorityForm(forms.ModelForm):
    class Meta:
        model = Priority
        fields = '__all__'

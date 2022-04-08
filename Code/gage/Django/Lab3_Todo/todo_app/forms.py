from django import forms
from django.forms import ModelForm
from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = NewTodoItem
        fields = '__all__'

class PriorityForm(forms.ModelForm):
    class Meta:
        model = TodoPriority
        fields = '__all__'
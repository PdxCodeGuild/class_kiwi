from django import forms
from .models import *
from django.forms import ModelForm
from todo_app.models import TodoItem


class todoitemform(ModelForm):
    class Meta:
        model = TodoItem
        fields = ['text', 'priority']

from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task        # Targets which model to create a form for
        fields = '__all__'  # Targets which fields to include from the model 
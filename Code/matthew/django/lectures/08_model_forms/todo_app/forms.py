from django import forms
from django.forms import ModelForm
from . models import *

# naming convention: Task() is model so this is TaskForm
class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        # 
        fields= '__all__'
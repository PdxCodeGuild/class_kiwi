
from django import forms
from django.forms import ModelForm
from .models import NewTask

class NewTaskForm(forms.ModelForm):
    class Meta:
        model= NewTask
        fields= "__all__"
class NewPriority(forms.ModelForm):
    class Meta:

        fields= "__all__"

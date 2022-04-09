
from django import forms
from django.forms import ModelForm
from .models import NewTask, Priority

class NewTaskForm(forms.ModelForm):
    class Meta:
        model= NewTask
        fields= "__all__"
class NewPriority(forms.ModelForm):
    class Meta:
        model= Priority
        fields= "__all__"

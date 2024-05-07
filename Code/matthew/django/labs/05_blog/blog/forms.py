from django import forms
from .models import BlogPost

class PostForm(forms.Form):
    title= forms.CharField(max_length=20)
    body= forms.CharField(max_length=120)
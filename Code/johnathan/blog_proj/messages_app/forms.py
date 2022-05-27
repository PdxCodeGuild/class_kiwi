from django import forms 

class NewPostform(forms.Form):
    text = forms.CharField(label='Posts', max_length=120)
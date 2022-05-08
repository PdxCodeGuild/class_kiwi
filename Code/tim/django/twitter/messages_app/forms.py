from django import forms

class NewTweetForm(forms.Form):
    text = forms.CharField(label='Tweet', max_length=20)
from django import forms

priority_choices = (('high', 'High'), ('medium', 'Medium'), ('low', 'Low'))


class NewTodoForm(forms.Form):
    text = forms.CharField(max_length=120)
    priority = forms.ChoiceField(choices=priority_choices)

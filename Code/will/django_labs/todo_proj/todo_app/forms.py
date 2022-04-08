from django import forms
from django_labs.todo_proj.todo_app.models import Priority


class NewTodoForm(forms.Form):
    text = forms.CharField(label='todo', max_length=120)
    priority = Priority()

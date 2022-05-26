from django import forms
from .models import *
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class NewTodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ("text", "priority")


class DateInput(forms.DateInput):
    input_type = "date"


class CalanderForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ("completed",)
        widgets = {
            "completed": DateInput(),
        }

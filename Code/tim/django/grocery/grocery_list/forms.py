from django import forms
from .models import GroceryItem


class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ('groceryitem','completed')
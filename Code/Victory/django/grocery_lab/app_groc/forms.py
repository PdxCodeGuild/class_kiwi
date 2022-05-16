from django import forms

from app_groc.models import StoreDepartment,Item 

class StoreDepForm(forms.ModelForm):
    class Meta:
        model = StoreDepartment
        fields = '__all__'

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item 
        fields = '__all__'
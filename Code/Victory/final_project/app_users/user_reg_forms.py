from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import *


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='First Name',  max_length=35)
    last_name = forms.CharField(label='Last Name', max_length=35)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username','password1', 'password2')

    def save(self, commit=True):
        user = super(AdminRegisterForm, self).save(commit=True)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # self.fields['occupation'].empty_label = "Select"
        if commit:
            user.save()
        return user

class DoctorRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='First Name',  max_length=35)
    last_name = forms.CharField(label='Last Name', max_length=35)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username','password1', 'password2')

    def save(self, commit=True):
        user = super(DoctorRegisterForm, self).save(commit=True)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # self.fields['occupation'].empty_label = "Select"
        if commit:
            user.save()
        return user

class BillerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label='First Name',  max_length=35)
    last_name = forms.CharField(label='Last Name', max_length=35)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username','password1', 'password2')

    def save(self, commit=True):
        user = super(BillerRegisterForm, self).save(commit=True)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # self.fields['occupation'].empty_label = "Select"
        if commit:
            user.save()
        return user



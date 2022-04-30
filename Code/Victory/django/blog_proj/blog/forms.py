from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegForm(UserCreationForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(label = 'First Name', max_length=20)
    last_name = forms.CharField(label = 'Last Name', max_length=20)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        
        return user

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        # fields = ('title', 'slug', 'body', 'image')
        fields = ('title', 'body', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            # 'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = ('title', 'body')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


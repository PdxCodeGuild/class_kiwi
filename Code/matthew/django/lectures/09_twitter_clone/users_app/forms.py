from django import forms

class NewSignUpForm(forms.Form):
    username= forms.CharField(label='Username', max_length=20)
    # widget=forms.PasswordInput hides characters
    password= forms.CharField(widget=forms.PasswordInput, label='Password', max_length=10)
    first_name= forms.CharField(label='First Name', max_length=20)
    last_name= forms.CharField(label='Last Name', max_length=20)
    email= forms.EmailField(label='Email')

class NewLoginForm(forms.Form):
    username= forms.CharField(label='Username', max_length=20, )
    password= forms.CharField(widget=forms.PasswordInput, label='Password', max_length=10)
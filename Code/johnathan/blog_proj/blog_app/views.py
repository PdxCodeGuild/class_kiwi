from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = NewSignupForm()
        form = NewSignupForm()
        return render(request, 'blog_app/signup.html', {
                'form': form
            })

    elif request.method == 'POST':
        form = NewSignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )
    
        return HttpResponseRedirect(reverse('signup'))

def user_login(request):
    if request.method == 'GET':
        return render(request, 'blog_app/login.html', {
            'form': NewLoginForm()
        })
    elif request.method == "POST":
        form = NewLoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(request, username=form.cleaned_data['username'], password = password)
            if user is None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                form.add_error('username', 'Invalid Credential')
                return render(request, 'blog_app/login.html', {
                    'form': form 
                })
def profile(request):
    return render(request, 'blog_app\profile.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from messages_app.models import Tweet

# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = NewSignupForm()
        return render(request, 'users_app/signup.html', {
        'form': form
        })
    
    elif request.method == 'POST':
        form = NewSignupForm(request.POST)
        if form.is_valid():
            #create a new user
            user = User.objects.create_user(
                username= form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'], 
                password= form.cleaned_data['password']
            )
        return HttpResponseRedirect(reverse('signup'))
            
    
def user_login(request):
    if request.method=='GET':
        return render(request, 'users_app/login.html', {
            'form':NewLoginForm()        })
        
    elif request.method == 'POST':
        form =NewLoginForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = authenticate(request, username=form.cleaned_data['username'], password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
            else:
                form.add_error('username', 'Invalid Credentials')
                return render(request, 'users_app/login.html', {
                    'form':form
                })
            
def profile(request):
    tweets = Tweet.objects.all().filter(user=request.user)
    return render(request, 'users_app/profile.html', {
        'tweets': tweets
    })

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
    
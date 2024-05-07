

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# import @login_required
from django.contrib.auth.decorators import login_required
# import Tweet model from messages app
from messages_app.models import Tweet

# Create your views here.
def signup(request):

    if request.method == "GET":
        form= NewSignUpForm()
        return render(request, 'users_app/signup.html', {
        'form':form
    })
    elif request.method == "POST":
        form= NewSignUpForm(request.POST)
        if form.is_valid():
            # create a new user
            user= User.objects.create_user(
                username= form.cleaned_data['username'],
                first_name= form.cleaned_data['first_name'],
                last_name= form.cleaned_data['last_name'],
                email= form.cleaned_data['email'],
                password= form.cleaned_data['password']
            )
            user.save()
        return HttpResponseRedirect(reverse('user:login'))

def user_login(request):
    if request.method == "GET":
        return render(request, 'users_app/login.html', {
            'form': NewLoginForm()
        })
    elif request.method == "POST":
        form= NewLoginForm(request.POST)
        if form.is_valid():
            password= form.cleaned_data['password']
            user= authenticate(request, username=form.cleaned_data['username'], password=password)
            # authenticate returns either authenticated or none
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))

            # if the user has not been authenticated
            else:
                form.add_error('username', 'Invalid Credentials')
                return render(request, 'users_app/login.html', {
                    'form': form
                })

def profile(request):
    # filtering through all Tweet objects for ones the user posted

    tweets= Tweet.objects.all().filter(user=request.user)

    context= {
        'tweets': tweets
    }
    return render(request, 'users_app/profile.html', context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))


from django.shortcuts import render
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect

# Login/Signup functions
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from messages_app.models import Tweet
 

# Sign up

def signup(request):
    # Displays before form input
    if request.method == 'GET':
        form = NewSignUpForm()
        context = {'form': form}
        return render(request, 'users_app/signup.html', context)
    # Creates a new User
    elif request.method == 'POST':
        form = NewSignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                password = form.cleaned_data['password'],
                email = form.cleaned_data['email'],
            )
        return HttpResponseRedirect(reverse('users:signup'))



# Login/Logout

def user_login(request):
    if request.method == 'GET':
        context = {'log_form': NewLoginForm()}
        return render(request, 'users_app/login.html', context)
    elif request.method == 'POST':
        log_form = NewLoginForm(request.POST)
        if log_form.is_valid():
            password = log_form.cleaned_data['password'] # Clears any empty spaces and removes them
            user =  authenticate(request, username=log_form.cleaned_data['username'], password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
            else:
                log_form.add_error('username', 'Invalid email or password')
                return render(request, 'users_app/login.html', {'log_form': log_form})
            

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))



# Profile page
@login_required
def profile(request):
    tweets = Tweet.objects.all().filter(user=request.user)
    context = {'tweets': tweets}
    return render(request, 'users_app/profile.html', context)

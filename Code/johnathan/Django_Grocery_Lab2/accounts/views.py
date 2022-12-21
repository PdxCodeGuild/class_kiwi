from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            try:
                User.objects.get(username=username)
                messages.error(request, 'User already exists')
            except User.DoesNotExist:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Signup success')
                return redirect('signin')
        else:
            messages.error(request, "Username or Password is missing!")
    return render(request, 'signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')

    redirect_url = request.GET.get('next')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if redirect_url:
                    return redirect(redirect_url)
                return redirect('index')
            else:
                messages.error(request, 'Incorrect username or password!')
                return redirect(f'/accounts/signin?next={redirect_url}')
        messages.error(request, "Username or Password is missing!")
    return render(request, 'signin.html')


@login_required
def signout(request):
    logout(request)
    messages.info(request, "Logged out!")
    return redirect('signin')


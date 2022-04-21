from django.shortcuts import render
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def signup(request):
    if request.method == 'GET':
        form = NewSignupForm()
        form = NewSignupForm()
        return render(request, 'blog_app/signup.html', {
                'form': form
            })

    elif request.method == 'POST':
        form = NewSignupForm(request)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
            )
    
        return HttpResponseRedirect(reverse('signup'))
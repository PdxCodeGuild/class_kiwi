from pickle import GET
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from secrets import choice
import random
import string
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'Password_app/index.html')

def result(request):
    number = int(request.POST['name'])
    
    
    while True:
        if 7 < number < 17:
            break
        else: 
            # return render(request, 'Password_app/index.html')
            return HttpResponseRedirect(reverse('Password_app:index'))
        
    password = list()
    char = string.ascii_letters
    for x in range(number):
        character = random.choice(char)
        password.append(character)
        print(password)
        
    
    return render(request, 'Password_app/result.html', {'password': password})
from django.shortcuts import render

import random
# Create your views here.
def index(request):
    return render(request, 'password_app/index.html')

def password(request):
    genPassword = ''
    length = 14
    length = int(length)
    characters = list('abcdefghijklmnopqrstuvwxyz£$%^&*!{}()ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    i=0
    while i < length:
        i=i+1
        genPassword = genPassword + random.choice(characters)
    return render(request, 'password_app/password.html', {'password': genPassword})

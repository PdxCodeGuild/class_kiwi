
from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.

def encode(request, name):
    # return HttpResponse(f'Hello {name}!')
    return render(request, 'rot13/index.html', {'name':name})




from django.http import HttpResponse
from django.shortcuts import render

#Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello World<h1/>')

def bruce(request):
    return HttpResponse('Hello Bruce')

def batman(request):
    return HttpResponse('sup bruce we know youre batman')

def say_hello(request, name):
    # return HttpResponse(f'Hello {name}!')
    return render(request, 'hello_app/index.html', {'name':name})
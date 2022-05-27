from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello(request):
    return HttpResponse('<h1>Hello World</h1>')

def bruce(request):
    return HttpResponse('<h1> Hello Bruce </h1>')

def say_hello(request, name):
    # return HttpResponse(f'Hello {name}! how are you?'

    return render(request, 'hello_app/index.html', {'name': name})
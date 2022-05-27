from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
# import http response from django
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse('<h1>Hello World <h1/>')


def bruce(request):
    return HttpResponse('Hello Bruce')


def batman(request):
    return HttpResponse('We know your batman')


def say_hello(request, name):
    # return HttpResponse(f'hello {name}')

    # calling index.html
    return render(request, 'hello_app/index.html', {'name': name})

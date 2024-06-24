from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello World</>')

def bruce(request):
    return HttpResponse('Hello Bruce')
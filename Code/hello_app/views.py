from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('<h1> Hello World </>')

def bruce(request):
    return HttpResponse("hello Bruce")

def batman(request):
    return render(request, 'hello_app/index.html', {'name':name})





from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('<h1>Hello World<h1/>')

def bruce(request):
    return HttpResponse("Hello Bruce")

def batman(request): 
    return HttpResponse("Sup Bruce, we know you're Batman.")

def say_hello(request, name):
    # return HttpResponse(f'hello {name}')
    return render(request, 'hello_app/index.html', {'test': name})




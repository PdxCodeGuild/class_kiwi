from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bio(request):
    return render(request, 'routing_app/bio.html')

def animations(request):
    return render(request, 'routing_app/animations.html')

def blog(request):
    return render(request, 'routing_app/blog.html')

def company(request):
    return render(request, 'routing_app/company.html')


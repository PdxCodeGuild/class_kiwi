from django.http import HttpResponse
from django.urls import path
from flask import request
from . import views

urlpatterns = [
    # path('bruce', views.bruce, name='bruce')    
    
    def say_hello(request, name):
        return render(request, 'hello_app/index.html', {'test':name})
]
from django.urls import path
from . import views 
from django.contrib import admin

urlpatterns = [
    #/8000
    path('', views.hello, name='hello'),

    #/8000/bruce
    path('bruce', views.bruce, name='bruce'),
    #8000/batman
    path('batman', views.batman, name ="batman"),
    #8000/stringname
    path('<str:name>', views.say_hello, name ="say_hello"),

    
]
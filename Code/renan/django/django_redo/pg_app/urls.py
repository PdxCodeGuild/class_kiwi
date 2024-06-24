from django.shortcuts import render
from django.urls import path 
from . import views



urlpatterns = [
    #manage 8000/
    path('',views.index, name='index') 
                  
 ]
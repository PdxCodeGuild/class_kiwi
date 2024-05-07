"""routing_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

"""

from django.urls import path
from . import views

urlpatterns = [
    path('bio/', views.bio, name='bio'),
    path('animation/', views.animation, name='animation'),
    path('blog/', views.blog, name='blog'),
    path('', views.base, name='base'),
    path('company/', views.company, name='company')
]
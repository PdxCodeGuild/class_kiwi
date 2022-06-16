from django.contrib import admin
from django.urls import path,include
from .import views

app_name = 'one_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
]
from django.urls import path 
from .import views

urlpatterns = [
    path('bio/', views.bio, name='bio'),

    path('animations/', views.animations, name='animations'),

    path('blog/', views.blog, name='blog'),

    path('company/', views.company, name='company'),
    
    path ('', views.base, name = 'base')]


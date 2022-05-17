from django import views
from django.urls import path
from .import views

urlpatterns = [
  
    #path('', views.index, name='index'),
    path('', views.index, name='index2'),
    path('save/', views.save_cheep, name='save')

]


#path('save/', views.save_cheep, name='save')
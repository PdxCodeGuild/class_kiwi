from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('add/<str:pk>', views.add, name='add'),
   
]
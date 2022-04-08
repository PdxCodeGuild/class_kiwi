from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('additem/', views.add_item, name='add_item'),
]
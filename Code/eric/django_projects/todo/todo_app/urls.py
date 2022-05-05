from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('saved_todos', views.new_todo, name='new_todo'),
]
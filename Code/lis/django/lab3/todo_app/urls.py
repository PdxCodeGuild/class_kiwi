from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_todo/<str:pk>', views.deleteTodo, name='delete_todo')
]

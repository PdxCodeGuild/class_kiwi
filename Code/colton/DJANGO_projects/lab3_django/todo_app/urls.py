from django.urls import path
from . import views


app_name = "todolist"

urlpatterns = [
    path("todo/", views.Todo, name="todo"),
    path("add/", views.addTodo, name="add"),
    path("complete/<str:pk>", views.completeTodo, name="complete"),
    path("delete/<str:pk>", views.deleteTodo, name="delete"),
]

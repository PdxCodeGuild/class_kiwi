from django.urls import path
from .import views

app_name = 'todo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('strike/<str:pk>/', views.strike_item, name='strike_item'),
    path('delete_todo/<str:pk>/', views.deleteTodo, name='delete_todo')
]

from django.urls import path
from . import views

app_name = 'todo_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.todo_list, name='todo_list'),
    path('create/', views.create_todo, name='create_todo'),
    path('toggle-complete/<int:todo_id>',
         views.toggle_complete, name='toggle_complete'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete-todo')
]

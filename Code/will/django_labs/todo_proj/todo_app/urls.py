from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save_task, name='save_task')
]

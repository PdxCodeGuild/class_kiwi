from django.urls import path
from .import views

app_name = 'modelforms'

urlpatterns = [
    path('', views.index, name='index'),
#     path('update/str:pk', views.updateTodo, name='update'),
#     path('delete/str:pk', views.deleteTodo, name='delete'),
    
]
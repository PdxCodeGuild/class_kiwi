from django.urls import path
from .import views

app_name = 'modelforms'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/str:pk', views.updateTask, name='update'),
    path('delete/str:pk', views.deleteTask, name='delete'),
    
]
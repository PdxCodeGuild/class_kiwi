from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'), 
    path('update/<str:pk>', views.updateTask, name='update'),
    path('delete/<str:pk>', views.deleteTask, name='delete'),
]
from django.urls import URLPattern, path
from . import views


app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>', views.updateTask, name='update'),
    path('delete/<str:pk>', views.deleteTask, name='delete'),
]
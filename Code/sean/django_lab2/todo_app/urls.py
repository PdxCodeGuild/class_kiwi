from django.urls import path
from .import views

app_name = "todo_app"

urlpatterns = [
    path('', views.index, name='index'),
    path ('delete/<str:pk>', views.delete, name='delete'),
    path('update/<str:pk>', views.update, name='update')
]
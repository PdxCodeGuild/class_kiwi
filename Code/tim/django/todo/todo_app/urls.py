from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('save_todo_item', views.new_todo, name='new_todo'),
]
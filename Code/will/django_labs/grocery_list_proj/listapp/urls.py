from django.urls import path
from . import views

app_name = 'listapp'
urlpatterns = [
    path('', views.index, name='index')
]

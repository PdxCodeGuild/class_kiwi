from django.urls import path, include
from . import views

app_name = 'rot'

urlpatterns = [
    # 127.0.0.1:8000
    path('', views.index, name='index'),


    path('/rot/', views.rot, name='rot')

   

]
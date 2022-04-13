from django.urls import path, include
from . import views

urlpatterns = [

    #manage 8000/
    path('', views.index, name='index'),

    #manage 8000/password
    path('length<int>', views.generate_password),
]
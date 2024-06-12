from django.urls import path, include
from . import views

urlpatterns = [

    #manage 8000/
    path('',views.index, name='index'),

    #manage 8000?
    path('result/', views.result, name='result' )
]

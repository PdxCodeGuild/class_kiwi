from django.urls import path
from . import views

app_name = 'ntp'
urlpatterns = [

    #8000/ntp
    path('', views.index, name='index'),

    #8000/ntp/result/<num>
    path('result/', views.result, name='result'),
]
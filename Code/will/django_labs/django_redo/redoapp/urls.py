from django.urls import path
from . import views

app_name = 'redoapp'
urlpatterns = [
    path('', views.unitcon, name='unitcon'),

    path('result/', views.result, name='result')

]

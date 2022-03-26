from django.urls import path
from . import views

app_name = 'lab1_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results')
]

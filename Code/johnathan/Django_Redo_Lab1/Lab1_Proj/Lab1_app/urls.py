from django.urls import path, include
from . import views

app_name = 'Lab1_app'

urlpatterns = [
    #8000/Lab1/Lab1_view
    path('Lab1_view/', views.Lab1_view, name='Lab1_view'),

    #8000/Lab1/rot13            results/<str:choice>
    path('rot13/', views.rot13, name='rot13')
]

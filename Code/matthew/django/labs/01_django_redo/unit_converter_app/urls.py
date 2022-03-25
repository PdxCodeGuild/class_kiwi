from django.urls import path, include
from . import views
# . :importing the views from the views file in the same directory

#
app_name = 'unit converter'

urlpatterns = [
    # 8000/ucp
    path('', views.index, name='index'),


    path('result/', views.forms, name='forms')

    # 8000/rps/result
    # path('result/', views.result, name='result'),

]

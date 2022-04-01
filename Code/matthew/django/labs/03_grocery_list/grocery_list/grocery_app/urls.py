"""grocery_app URL Configuration

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')

"""
from . import views
from django.urls import path

urlpatterns = [
    # /list
    path('list/', views.home, name='home' ),
    path('save/', views.save, name='save' )
]

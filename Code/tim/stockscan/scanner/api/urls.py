from django.urls import path
from .views import main

urlpatterns = [
    path('home', main),
    path('', main),

]
from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
    path('grocery_view/', views.grocery_view, name='grocery_view'),

    path('grocery_order/', views.grocery_order, name='grocery_order')
]
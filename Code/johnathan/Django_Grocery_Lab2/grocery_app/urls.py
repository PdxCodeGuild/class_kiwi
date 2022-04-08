from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
    path('view/', views.grocery_view, name='grocery_view'),

    path('order/', views.grocery_order, name='grocery_order')
]
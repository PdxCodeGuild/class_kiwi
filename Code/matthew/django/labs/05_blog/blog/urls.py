from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('new/', views.new_post, name="new_post"),
    path('view/<int:id>', views.view_post, name="view_post"),
]

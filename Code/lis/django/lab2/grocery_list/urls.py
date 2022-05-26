from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [

    path('', views.index, name='index'),
    path('save/', views.save_grocery_item, name='save'),
    path('delete/<int:grocery_item>/', views.delete_grocery_item, name='delete'),
    path('update/<int:grocery_item>/', views.update_grocery_item, name='update')
]

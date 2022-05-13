from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [

    path('', views.index, name='index'),
    path('save/', views.save_grocery_item, name='save'),
    path('delete/<int:grocery_item>/', views.delete_grocery_item, name='delete'),
    path('update_true/<int:grocery_item>/',
         views.update_grocery_item_true, name='update_true'),
    path('update_false/<int:grocery_item>/',
         views.update_grocery_item_false, name='update_false')
]

from django.urls import path 
from . import views

app_name = 'app_groc'
urlpatterns = [ 
    path('', views.index, name='index'),
    path('add/', views.add_prod, name='add'),
    path('complete/<int:prod_id>/', views.complete_prod, name='complete'),
    path('delete<int:prod_id>/', views.delete_prod, name='delete'),
]
from django.urls import path
from . import views

app_name = 'grocery_app'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.grocery_list, name = ' grocery_list'),

    path('', views.grocery_list, name ='grocery_list_by_category'),

    path('<int:id>/<slug:slug>/', views.grocery_details, name= 'grocery_detail')

]
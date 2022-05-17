from django.urls import URLPattern, path
from . import views

app_name = 'grocery_list'
# url pattern
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item', views.add_item, name='add'),

]

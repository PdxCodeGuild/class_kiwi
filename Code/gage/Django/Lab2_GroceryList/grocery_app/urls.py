from django.urls import path, URLPattern
from . import views

app_name = 'grocery'
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<str:pk>', views.updateItem, name='update'),
    path('remove/<str:pk>', views.removeItem, name='remove')
]
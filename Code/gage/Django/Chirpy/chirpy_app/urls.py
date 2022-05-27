from django.urls import URLPattern, path
from . import views

app_name = 'chirpy'
urlpatterns = [
    path('', views.index, name='index1'),
    path('save/', views.save_cheep, name='save')
]
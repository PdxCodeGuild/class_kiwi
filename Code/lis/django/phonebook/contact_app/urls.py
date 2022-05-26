from django.urls import path
from .import views

app_name = 'contacts'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('all/', views.all_contacts, name='all_contacts'),
    path('save_contact/', views.save_contact, name='save_contact'),
    path('search/', views.search_contact, name='search_contact'),

]

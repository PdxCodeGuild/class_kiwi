"""contact_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name= 'contacts'

urlpatterns = [
    # contacts/
    path('', views.home_page, name='home'),
    # contacts/all/
    path('all/', views.all_contacts, name='all'),
    # contacts/save_contact form submission 
    path('save_contact/', views.save_contact, name='save'),
    path('search/', views.search_contact, name='search'),
]

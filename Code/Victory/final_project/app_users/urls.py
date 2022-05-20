from django.urls import path 
from . import views

urlpatterns = [ 
    path('', views.index, name='home'),
    path('adminreg/', views.admin_register, name='adminreg'),
    path('billerreg/', views.biller_register, name='billerreg'),
    path('doctorreg/', views.doctor_register, name='doctorreg'),

    path('adminlog/', views.admin_login, name='adminlog'),
    path('doclog/', views.doc_login, name='doclog'),
    path('billerlog/', views.biller_login, name='billerlog'),
]
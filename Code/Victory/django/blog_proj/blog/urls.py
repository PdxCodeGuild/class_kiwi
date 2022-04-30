from django.urls import path 
from blog.views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('create/', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    # path('<int:pk>/edit/', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('<int:pk>/', BlogDetailView.as_view(),name='blog_detail')
    
]
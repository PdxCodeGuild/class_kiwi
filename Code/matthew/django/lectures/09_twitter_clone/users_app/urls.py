
"""twiter_app URL Configuration

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
app_name= 'user'
urlpatterns = [
    # users/signup/
    path('signup/', views.signup, name='signup'),
    # users/login/
    path('login/', views.user_login, name='login'),
    # users/profile/
    path('profile/', views.profile, name='profile'),
    # users/logout/
    path('logout/', views.user_logout, name='logout'),
    

]

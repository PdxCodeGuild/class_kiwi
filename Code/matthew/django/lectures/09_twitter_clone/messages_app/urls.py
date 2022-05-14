"""messages_app URL Configuration

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
app_name= 'messages'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_tweet, name='new_tweet'),
    path('delete/<int:tweet_id>', views.del_tweet, name='del_tweet'),
    path('like/<int:tweet_id>', views.like, name='like'),
    path('dislike/<int:tweet_id>', views.dislike, name='dislike'),
    path('detail/<int:tweet_id>', views.detail, name='detail'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_tweet, name='new_tweet'),
    path('delete/<int:tweet_id>', views.delete_tweet, name='delete_tweet'),
    path('like/<int:tweet_id>', views.like_tweet, name='like_tweet'),
    path('dislike/<int:tweet_id>', views.dislike_tweet, name='dislike_tweet'),
    path('detail/<int:tweet_id>', views.detail, name='detail'),

]
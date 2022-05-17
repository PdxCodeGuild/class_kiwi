from django.urls import path
from .import views
urlpatterns = [
 
    path('', views.index, name='index' ), 
    path('new/', views.new_tweet, name='new_tweet' ), 
    path('delete/<int:tweet_id>', views.delete_tweet, name='delete_tweet' ), 
    path('like/<int:tweet_id>', views.like, name='like' ),
    path('dislike/<int:tweet_id>', views.dislike, name='dislike' ),
    path('detail/<int:tweet_id>', views.detail, name='detail' ),
    
]
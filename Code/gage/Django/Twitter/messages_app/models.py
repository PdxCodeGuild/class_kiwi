from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets') # CASCADE will delete all users data(posts) if the user no longer exists
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=1)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.text[:15]}, Posted: {self.published_date.month}/{self.published_date.day}/{self.published_date.year}" # {self.text[:15]} slices the tweet to only show the first 15 chars in admin panel


class Reply(Tweet):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='replies')

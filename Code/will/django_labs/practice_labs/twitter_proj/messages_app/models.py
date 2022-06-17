from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    text = models.CharField(max_length=120)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tweets')
    likes = models.IntegerField(default=1)
    dislikes = models.IntegerField(default=0)
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}: {self.text[:15]} {self.published_date.year}/{self.published_date.month}/{self.published_date.day}'

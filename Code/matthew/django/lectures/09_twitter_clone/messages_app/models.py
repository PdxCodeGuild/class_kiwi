from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tweet(models.Model):
    text= models.CharField(max_length=120)
    # related_name: ?
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=1)
    # auto_now=True updates everytime the field is updated or modified
    # auto_now_add=True updates when created
    pub_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text[:15]} {self.pub_date.year}/{self.pub_date.month}/{self.pub_date.day} '

# inheriting tweet characteristics/Properties
class Reply(Tweet):
    # create relationship between Reply and Tweet
    tweet= models.ForeignKey(Tweet,on_delete=models.CASCADE, related_name='replies')
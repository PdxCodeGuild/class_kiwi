from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title= models.CharField(max_length=10)
    body= models.TextField(max_length=120)
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    public= models.BooleanField(default=False)
    date_created= models.DateTimeField(auto_now_add=True)
    date_edited= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} -- {self.body[:10]}'


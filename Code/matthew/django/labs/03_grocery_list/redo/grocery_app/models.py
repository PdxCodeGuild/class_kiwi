from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class List(models.Model):
    new= models.CharField(max_length=50)
    date= models.DateField(auto_now=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    delete= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.new}: {self.date}'
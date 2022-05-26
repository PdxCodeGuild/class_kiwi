from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class GroceryItem(models.Model):
    item = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item}'

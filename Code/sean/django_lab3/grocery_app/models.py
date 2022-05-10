from django.db import models
from django.forms import BooleanField

# Create your models here.

class GroceryItem(models.Model):
    item = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item

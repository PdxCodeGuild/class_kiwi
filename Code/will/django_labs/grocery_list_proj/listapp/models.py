from django.db import models

# Create your models here.


class GroceryItem(models.Model):
    item_descrip = models.CharField(max_length=200)

    completed = models.BooleanField(default=False)

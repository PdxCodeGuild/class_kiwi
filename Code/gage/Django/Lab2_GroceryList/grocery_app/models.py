from django.db import models

# Create your models here.

class GroceryItem(models.Model):
    item = models.CharField(max_length=25)
    complete = models.BooleanField(default=False)
    order = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item
from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    groceryitem = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    # def __str__(self):
    #     return self.groceryitem
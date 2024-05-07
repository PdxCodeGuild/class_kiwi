from django.db import models

# Create your models here.
class Department(models.Model):
    name= models.CharField(max_length=20)
    def __str__(self):
        return f'{self.name}'

class GroceryItem(models.Model):
    item= models.CharField(max_length=40)
    completed= models.BooleanField(default=False)
    # create a relationship between Class Department and GroceryItem
    # Each GroceryItem belongs to a "department"
    # related name lets you call items from GroceryItem from Department.item
    department= models.ForeignKey(Department, on_delete=models.CASCADE, related_name='item', null=True, blank=True )
    def __str__(self):
        return f'{self.item} -- {self.completed}'
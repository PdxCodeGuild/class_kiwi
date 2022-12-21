from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'
class GroceryItem(models.Model):
    item = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= 'items', null=True, blank=True) 
    
    #empty fields to manage empty value in a database; value on a form can be blank

    def __str__ (self):
        return f'{self.item} -- {self.completed}'
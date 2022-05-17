
from django.db import models
from django.contrib.auth.models import User
    
class Department(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name}'
    
class GroceryItem(models.Model):
    item = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    
    def __str__(self):
        return f'{self.item} -- {self.completed}'
    
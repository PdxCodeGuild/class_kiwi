from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    grocery = models.CharField(max_length=120)
    def __str__(self):
        return f'{self.grocery}'

class GroceryItem(models.Model):
    item = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    date_published = models.DateTimeField(auto_now=True)  
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='items', null=True, blank=True) 
    
    def __str__(self):
        return f'{self.item} -- {self.completed}'
    
 
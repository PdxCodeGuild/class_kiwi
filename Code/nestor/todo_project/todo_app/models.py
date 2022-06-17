from email import charset
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.forms import CharField


# Create your models here.
class Priority(models.Model):
    item = models.CharField(max_length=120)
    
    def __str__(self):
        return f'{self.item}'
    
class TodoItem(models.Model):
    text = models.CharField(max_length=120)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='related')
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.text} -- {self.priority}'
    
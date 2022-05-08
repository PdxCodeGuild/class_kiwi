from django.db import models
from django.contrib.auth.models import User
from django.forms import NullBooleanField
# Create your models here.
PRIO_CHOICES = (
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)
class ToDo(models.Model):
    text = models.CharField(max_length=120, )
    priority = models.CharField(max_length=6, choices=PRIO_CHOICES, default='medium')
    completed = models.BooleanField(null=True)    
    
    created_date = models.DateTimeField(auto_now=True)


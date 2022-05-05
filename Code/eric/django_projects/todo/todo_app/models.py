from django.db import models
from django.contrib.auth.models import User
# Create your models here.
PRIO_CHOICES = (
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)
class ToDo(models.Model):
    text = models.CharField(max_length=120, )
    priority = models.CharField(max_length=6, choices=PRIO_CHOICES, default='medium')
        
    
    created_date = models.DateTimeField(auto_now=True)

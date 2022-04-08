from django.db import models

# Create your models here.
priority_choices = (('high', 'HIGH'), ('medium', 'MEDIUM'), ('low', 'LOW'))


class Priority(models.Model):

    name = models.CharField(
        max_length=6, choices=priority_choices, defaul='low')


class TodoItem(models.Model):

    text = models.CharField(max_length=120, label='todo item')
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name='priority')
    created_date = models.DateTimeField(auto_now=True)

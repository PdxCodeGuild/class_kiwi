from django.db import models


# Create your models here.


class Priority(models.Model):
    PRIORITIES_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),

    ]
    prior = models.CharField(
        max_length=100, choices=PRIORITIES_CHOICES)

    def __str__(self):
        return self.prior


class TodoItem(models.Model):

    text = models.CharField(max_length=100)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name='todoitems')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text} : {self.priority} : {self.created_date.year} : {self.created_date.month} : {self.created_date.day}'

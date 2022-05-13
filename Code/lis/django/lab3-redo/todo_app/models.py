from django.db import models


# Create your models here.

CHOICES = [
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]


class Priority(models.Model):
    name = models.CharField(
        max_length=10, choices=CHOICES, default='Medium')

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=100)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name='priority')
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.text}, {self.priority.name}'

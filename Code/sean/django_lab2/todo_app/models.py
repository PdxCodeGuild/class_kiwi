from django.db import models


# Create your models here.

CHOICES = [
    ('High','High'),
    ('Medium','Medium'),
    ('Low','Low'),
]

class Todo(models.Model):
    title = models.CharField(max_length=40,)
    priority = models.CharField(max_length=6, choices=CHOICES)
    cool = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.priority}'

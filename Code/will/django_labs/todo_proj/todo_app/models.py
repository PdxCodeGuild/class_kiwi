from django.db import models
# Create your models here.


class Priority(models.Model):

    name = models.CharField(
        max_length=6, choices=(('high', 'High'), ('medium', 'Medium'), ('low', 'Low')), default='low')


class TodoItem(models.Model):
    text = models.CharField(max_length=120)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text} {self.priority} {self.created_date.day}'

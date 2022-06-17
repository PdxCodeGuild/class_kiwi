from django.db import models
# Create your models here.


class Priority(models.Model):
    name = models.CharField(
        max_length=6, choices=(('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')))

    def __str__(self):
        return f'{self.name}'


class TodoItem(models.Model):
    text = models.CharField(max_length=120)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, related_name='items')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.text} {self.created_date.month}/{self.created_date.day}'

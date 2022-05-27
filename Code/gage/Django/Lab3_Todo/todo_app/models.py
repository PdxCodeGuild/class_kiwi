from django.db import models
# Create your models here.
class NewTodoItem(models.Model):
    name = models.CharField(max_length=20)
    added = models.DateTimeField(auto_now=True)
    is_pri = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"

class TodoPriority(models.Model):
    priority = models.BooleanField(default=False)
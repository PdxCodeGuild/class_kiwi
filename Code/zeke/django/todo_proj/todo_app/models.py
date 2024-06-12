from django.db import models


# Create your models here.
PRIORITIES = [ 
    ("high", "High"),
    ("medium", "Medium"),
    ("low","Low"),
]
class Priority(models.Model):
    list = models.CharField(max_length=200, choices=PRIORITIES, default="low")


    def __str__(self):
      return f"{self.list}"

class TodoItem(models.Model):
    text= models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="todo")
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"{self.text}"
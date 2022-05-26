from django.db import models
from django.forms import DateTimeInput


High = "High"
Medium = "Medium"
Low = "Low"
# Create your models here.
choice_range = ((High, "High"), (Medium, "Medium"), (Low, "Low"))


class Priority(models.Model):
    name = models.CharField(max_length=6, choices=choice_range)

    def __str__(self) -> str:
        return f"{self.name}"


class TodoItem(models.Model):
    text = models.CharField(max_length=60)
    priority = models.ForeignKey(
        Priority,
        on_delete=models.CASCADE,
        related_name="todoitems",
    )
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        if self.completed == None:
            return f"{self.text}, Priority: {self.priority}"
        else:
            return f"{self.text}, Priority: {self.priority}, Completed: {self.completed.year}/{self.completed.month}/{self.completed.day}"

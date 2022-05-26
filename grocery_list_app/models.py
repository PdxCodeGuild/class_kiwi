from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Grocery(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.quantity} || {self.item}"

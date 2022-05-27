
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cheep(models.Model):
    chirp = models.CharField(max_length=120)
    date_published = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}: --{self.chirp}--: {self.date_published}"
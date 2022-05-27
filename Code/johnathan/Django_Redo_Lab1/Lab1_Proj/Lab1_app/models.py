from django.db import models

# Create your models here.
class Lab1_Model(models.Model):
    lab1_field = models.CharField(max_length=100)

    def __str__(self):
        return self.lab1_field


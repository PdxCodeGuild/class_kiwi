from django.db import models

# Create your models here.
class StoreDepartment(models.Model):

    store= models.CharField(max_length=30)

    def __str__(self):
        return f'{self.store}'

class Item(models.Model):

    item=models.CharField(max_length=20)
    done = models.BooleanField(default=False)
    section = models.ForeignKey(StoreDepartment, on_delete=models.CASCADE, related_name='products', null=True, blank=True)

    def __str__(self):
        return f"{self.item} - {self.done} "


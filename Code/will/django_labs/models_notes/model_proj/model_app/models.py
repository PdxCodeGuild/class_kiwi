from django.db import models

# Create your models here.


class Kiwi(models.Model):
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

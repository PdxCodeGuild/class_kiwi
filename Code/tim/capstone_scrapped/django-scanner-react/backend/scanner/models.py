from django.db import models

# Create your models here.

class Scan(models.Model):
    symbol = models.CharField(max_length=10)
    
    def _str_(self):
        return self.title

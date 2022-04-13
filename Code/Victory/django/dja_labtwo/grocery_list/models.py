from django.db import models
from django.utils import timezone

# STATUS = (
#     (0, 'No'),
#     (1, 'Yes')
# )

# Create your models here.
class Grocery(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

from django.db import models


PRIORITY_CHOICES = ( 

  ('1', 'Low'), 

  ('2', 'Medium'), 

  ('3', 'High'), 

) 
# Create your models here.

class Priority(models.Model):
    status = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.status


class Todo(models.Model):
    title = models.CharField(max_length=250) 
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True) 
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='todo') 


    def __str__(self): 

        return f'{self.title}' 












#     class Meta: 

#         ordering = ['-priority', 'title'] 

#     class Admin: 

#         pass

# class Meta:
# #         ordering = ['title']
# # # The class Admin bit allows us to set options for Django’s 
# # # automatic administrative interface, which we’ll see later. 
# # # The pass keyword tells Django to just use its defaults.
# #     class Admin:
# #         pass
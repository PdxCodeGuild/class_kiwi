from django.db import models



PRIORITY_CHOICES = ( 

  ('Low', 'Low'), 

  ('Medium', 'Medium'), 

  ('High', 'High'), 

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
    #priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name='todo')
    prioritychoice = models.CharField(max_length=10, choices=PRIORITY_CHOICES) 


    def __str__(self): 

        return f'{self.title}' 



 








from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
LVL= (
    (1,'Low'),
    (2,'Medium'),
    (3,'High'),
)
# Create your models here.
class NewTask(models.Model):
    task= models.CharField(max_length=25)
    complete= models.BooleanField(default=False)
    date= models.DateTimeField(auto_now=True)
    priority= models.IntegerField(default=0, blank=True, choices=LVL)
# trying to join priority and Newtask 
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=0)
    # object_id = models.PositiveIntegerField(default=False)
    # content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.task}'

# class Priority(models.Model):
#     importance= models.CharField(max_length=6,choices=LVL, default='Low') 
#     date= models.DateTimeField(auto_now=True)
#     # object_id = models.PositiveIntegerField()
#     def __str__(self):
#         return f'{self.importance}'








########################################################################################################

# class TaggedItem(models.Model):
#     tag = models.SlugField()
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type', 'object_id')

#     def __str__(self):
#         return self.tag

# from django.db import models

# class Grocery_Model(models.Model):
#     grocery_field = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.grocery_field

from django.conf import settings
from django.contrib.auth import get_user_model 
from django.db import models
from django.db.models.signals import post_save

from products.models import Product 

User = get_user_model(
)

class Grocery_Item(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    groceries = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.user.username

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Grocery_Item.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)



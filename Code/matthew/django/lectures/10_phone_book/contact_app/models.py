import email
from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name= models.CharField(max_length=15)
    # null=True and blank=True allows the field to be blank
    last_name= models.CharField(max_length=15, null=True, blank=True)
    phone_number= models.CharField(max_length=15, null=True, blank=True)
    email= models.EmailField(null=True, blank=True)
    address= models.CharField(max_length=100, null=True, blank=True)
    fav= models.BooleanField(default=False)

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'

    def full_name(self):
        # if self.last_name has a value
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.first_name}'

    def favorite(self):
        # if fav = True
        if self.fav:
            return 'a favorite'
        else: 
            return "not fav"

    def __str__(self):
        return f'{self.favorite()} -- {self.full_name()}'

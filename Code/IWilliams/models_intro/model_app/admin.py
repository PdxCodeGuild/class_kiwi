from django.contrib import admin

# Register your models here.


#import model class
from .models import Kiwi

#register our model
admin.site.register(Kiwi)
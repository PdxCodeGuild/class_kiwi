from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Grocery)

class Post(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'completed', 'date_completed')
    list_filter = ('date_created',)

    

admin.site.register(Grocery,Post)




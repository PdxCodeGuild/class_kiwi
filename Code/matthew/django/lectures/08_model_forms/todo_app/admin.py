from django.contrib import admin
# * imports all from models
from . models import *

# Register your models here.

admin.site.register(Task)

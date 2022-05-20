from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Occupation)
admin.site.register(Physician)
admin.site.register(CodeSpecialist)
admin.site.register(Patient)

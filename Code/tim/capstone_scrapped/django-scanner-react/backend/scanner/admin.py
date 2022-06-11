from django.contrib import admin
from .models import Scan


class ScanAdmin(admin.ModelAdmin):
    list_display = ('symbol',)
# Register your models here.

admin.site.register(Scan, ScanAdmin)    
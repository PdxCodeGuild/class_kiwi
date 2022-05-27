from django.contrib import admin
from .models import Item


# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'quantity', 'date',)
    ordering = ('-id',)
    search_fields = ('name',)
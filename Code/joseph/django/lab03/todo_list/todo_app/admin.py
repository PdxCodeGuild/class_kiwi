from django.contrib import admin
from todo_app.models import Priority, ToDoItem

# Register your models here.

admin.site.register(Priority)
admin.site.register(ToDoItem)

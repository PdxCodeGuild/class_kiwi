from django.shortcuts import render
from django.http import HttpResponse 
from .models import *

# Create your views here.

def mytodo(request):
    data = TodoItem.objects.all()
    context ={
        'message': 'TO DO LIST ',
        'data': data

    
        
    }
    return render(request, 'todo_app/mytemplate.html', context)



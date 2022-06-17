from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Priority, TodoItem
from .forms import *

# Create your views here.
def index(request):
    todos = TodoItem.objects.all()
    priorities = Priority.objects.all()
    
    context = {
        'todos': todos,
        'priorities': priorities
    }
    return render(request, 'todo_app/index.html', context)

def save(request):
    if request.method == 'POST':
        todo_text = request.POST['text']
        priority_id = request.POST['priority']
        new_item = TodoItem()
        new_item.text = todo_text
        if priority_id:
            priority = Priority.objects.get(id=priority_id)
            new_item.priority = priority
        new_item.save()
    return HttpResponseRedirect(reverse('todo_app:index'))

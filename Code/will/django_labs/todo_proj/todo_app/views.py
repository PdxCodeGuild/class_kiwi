from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    priorities = Priority.objects.all()
    tasks = TodoItem.objects.all().order_by('-created_date')
    return render(request, 'todo_app/index.html', {
        'tasks': tasks, 'priorities': priorities
    })


def save_task(request):
    task_text = request.POST['item']
    task_prio = request.POST['priority']
    new_task = TodoItem()
    new_task.text = task_text
    if task_prio:
        priority = Priority.objects.get(id=task_prio)
        new_task.priority = priority
    new_task.save()

    return HttpResponseRedirect(reverse('todo_app:index'))

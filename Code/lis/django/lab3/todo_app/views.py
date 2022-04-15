from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from todo_app.forms import *


# Create your views here.
def index(request):
    todos = TodoItem.objects.all().order_by('priority')
    form = TodoForm()

    context = {
        'todos': todos,
        'form': form
    }

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'todo_app/index.html', context)


def updateTodo(request, pk):
    todo = TodoItem.objects.get(id=pk)
    form = TodoForm(instance=todo)

    context = {
        'form': form
    }

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()

    return HttpResponseRedirect(reverse('todo_app:index', context))


def strike_item(request, pk):
    todo_item = TodoItem.objects.get(id=pk)
    todo_item.complete = not todo_item.complete
    todo_item.save()

    return HttpResponseRedirect(reverse('todo_app:index'))


def deleteTodo(request, pk):
    item = TodoItem.objects.get(id=pk)
    item.delete()

    return HttpResponseRedirect(reverse('todo_app:index'))

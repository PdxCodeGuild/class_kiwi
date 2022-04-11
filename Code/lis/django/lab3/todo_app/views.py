from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
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
            return redirect('/')

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
            return redirect('/')

    return render(request, 'todo_app/index.html', context)


def deleteTodo(request, pk):
    item = TodoItem.objects.get(id=pk)

    context = {
        'item': item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'todo_app/delete.html', context)


from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from todo_app.forms import TodoForm

# Create your views here.

def index(request):
    tasks = Todo.objects.all()
    form = TodoForm()

    # if request.method == 'POST':
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')

    context = {'tasks': tasks, 'form': form,}
    
    return render(request, 'todo_app/index.html', context)

def updateTodo(request, pk):
    task = Todo.objects.get(id=pk)
    form = TodoForm(instance = task)

    context = {'form': form}

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'todo_app/update.html', context)

def deleteTodo(request, pk):
    item = Todo.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
        
    context = {'item': item}

    return render(request, 'todo_app/delete.html', context)
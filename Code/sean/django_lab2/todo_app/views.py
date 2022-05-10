from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.

def index(request):

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    form = TodoForm()
    todos = Todo.objects.all()

    context = {'form': form, 
            'todos': todos}

    return render(request, 'todo_app/index.html', context)

def delete(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'POST':
        todo.delete()
        return redirect('/')

    form = TodoForm()
    context = {'form': form, 
            'todo': todo}
            
    return render(request, 'todo_app/delete.html', context)

def update(request, pk):
    
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {'form': form, 
            'todo': todo}
    return render(request, 'todo_app/update.html', context)

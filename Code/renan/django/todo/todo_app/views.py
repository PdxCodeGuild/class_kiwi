from multiprocessing import context
from django.shortcuts import render, redirect
from todo_app.forms import TaskForm
from .models import *
# Create your views here.
def index(request):
    
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()            
        return redirect('/')

        
    context = {'tasks': tasks, 'form':form}
    
    return render(request, 'todo_app/index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)   
    form = TaskForm(instance=task)
    
    context = {'form':form}
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')     
    return render(request, 'todo_app/update.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context = {'item':item}
    
    return render(request, 'todo_app/delete.html', context)
    
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from todo_app.forms import TaskForm 
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo')
    context =  {'tasks': tasks, 'form': form }
    return render(request, 'todo_app/index.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST': 
        form = TaskForm(request.POST, instance=task) #Instance targets the task object (will replace old task with new input)
        if form.is_valid():
            form.save()
            return redirect('/todo')
    context =  {'form': form}
    return render (request, 'todo_app/update.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/todo')

    context = {'item': item}
    return render (request, 'todo_app/delete.html', context)
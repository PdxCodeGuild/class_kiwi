from django.forms import BooleanField
from django.shortcuts import redirect, render
# from . models import Task
from . models import *
from todo_app.forms import TaskForm

# Create your views here.

def index(request):
    # tasks= Task.objects.all()
    tasks= Task.objects.filter(complete=False)
    done_tasks= Task.objects.filter(complete=True)
    form= TaskForm()

    if request.method == 'POST':
        form= TaskForm(request.POST)
        if form.is_valid():
            # .save() saves information to database
            form.save()
        return redirect('/')

    context= {
        'tasks': tasks,
        'done_tasks': done_tasks,
        'form': form
    }
    return render(request, 'todo_app/index.html', context)

def updateTask(request, pk):
    # targets specific id
    task= Task.objects.get(id=pk)
    # edit specifc id
    form= TaskForm(instance=task)
    context= {
        'form': form
    }
    if request.method == "POST":
        # specifically targeting the id=pk for the indavidual task 
        form= TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'todo_app/update.html', context)

def deleteTask(request, pk):
    item= Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context= {
        'item': item,
    }

    return render(request, 'todo_app/delete.html', context)
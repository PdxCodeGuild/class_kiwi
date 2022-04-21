from itertools import chain
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import NewTask
from .forms import NewTaskForm, NewPriority

# using iterrools chain() to combine NewTask obj w/ Priority obj in a list
# EX ['task1','low','task2','medium','task3','high']
# Does not combine obj.id: Can not call one obj and get the other

# Create your views here.
def home(request):
    # tasks= NewTask.objects.order_by("complete")
    tasks= NewTask.objects.all()
    form= NewTaskForm()

    if request.method == 'POST':
        form= NewTaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('home'))
    context= {
        'tasks': tasks,
        'form': form,


     }
    return render(request, 'todo_app/index.html', context)

def edit(request, pk):
    task=NewTask.objects.get(id=pk)


    form= NewTaskForm(instance=task)
    context= {
        'form':form,

    }
    if request.method == "POST":
        form= NewTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    return render(request, 'todo_app/edit.html', context)

def delete(request, pk):
    NewTask.objects.filter(id=pk).delete()
    return redirect(reverse('home'))



from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task= forms.CharField(label='new task')

tasks= []

# Create your views here.

def index(request):
    # .session tracks user by cookies
    # session is a request object
    # method is a request object
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'sessions_app/index.html', {
        'tasks': tasks
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task= form.cleaned_data['task']
            tasks.append(task)
            # request.session['tasks'] +=[task]

            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'sessions_app/add.html', {
                'form': form
            })
    return render(request, 'sessions_app/add.html', {
        'form': NewTaskForm()
    })

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django import forms

# Create your views here.

tasks = []


def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []

    return render(request, 'seshapp/index.html', {'tasks': tasks})


class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task', max_length=200)


def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            tasks.append(task)
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'seshapp/add.html', {
                'form': form
            })
    return render(request, 'seshapp/add.html', {
        'form': NewTaskForm()
    })

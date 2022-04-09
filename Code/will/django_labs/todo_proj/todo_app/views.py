from django.shortcuts import render
from .forms import *
from .models import TodoItem
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

tasks = [

]


def index(request):
    tasks = TodoItem.objects.all().order_by('-created_date')
    return render(request, 'todo_app/index.html', {
        'tasks': tasks, 'form': NewTodoForm()
    })


def save_task(request):
    form = NewTodoForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        tasks = TodoItem()
        tasks.text = forms.cleaned_data['text']
        tasks.priority = forms.cleaned_data['priority']
        tasks.save()

    return HttpResponseRedirect(reverse('index'))

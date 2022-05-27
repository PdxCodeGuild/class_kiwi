from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse
# Create your views here.

def index(request):
    form = TodoForm()
    list = NewTodoItem.objects.all().order_by('-added')
    pform = PriorityForm()
    context = {'form':form, 'list':list, 'pform':pform}
    return render(request, 'todo_app/index.html', context)

def add_item(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        pform = PriorityForm(request.POST)
        print(pform['priority'])
        
        if form.is_valid():
            if str(pform['priority']) == '<input type="checkbox" name="priority" id="id_priority" checked>':
                todo = NewTodoItem()
                todo.is_pri = True
                todo.name = form.cleaned_data['name']
                todo.save()
            else:
                todo = NewTodoItem()
                todo.is_pri = False
                todo.name = form.cleaned_data['name']
                todo.save()
                
                
        return HttpResponseRedirect(reverse('index'))

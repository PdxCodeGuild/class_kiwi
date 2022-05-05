from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import *
# Create your views here.

def index(request):
    if request.method == "GET":
        todos = ToDo.objects.all()
    return render(request, 'index.html',{
        'todos':todos,
        'form': ToDoForm,}
        )


# Create your views here.
def new_todo(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = ToDo()
            todo.priority = form.cleaned_data['priority']
            todo.text = form.cleaned_data['text']
            todo.save()
        return HttpResponseRedirect(reverse('index'))
    if request.method == "GET":
        form = ToDoForm()

        return render(request,'saved_todos.html', {'form': form} )
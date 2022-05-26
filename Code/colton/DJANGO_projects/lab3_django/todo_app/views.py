from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import *
from django.urls import reverse
from .models import *
from django import forms
import datetime


def Todo(request):
    items = TodoItem.objects.all().order_by("-created")[:20]
    priorities = Priority.objects.all()
    form = NewTodoForm()
    form2 = CalanderForm()

    context = {
        "form": form,
        "items": items,
        "priorities": priorities,
        "form2": form2,
        "time": datetime.datetime.today(),
    }
    return render(request, "todo_app/todo.html", context)


def addTodo(request):

    form = NewTodoForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            text = form.cleaned_data["text"]
            priority = form.cleaned_data["priority"]

            items = TodoItem()
            items.text = text
            items.priority = priority

            items.save()

    return HttpResponseRedirect(reverse("todolist:todo"))


def completeTodo(request, pk):
    item = TodoItem.objects.get(id=pk)
    form2 = CalanderForm(instance=item)
    if request.method == "POST":

        form2 = CalanderForm(request.POST, instance=item)
        if form2.is_valid():
            form2.save()

    return redirect(reverse("todolist:todo"))


def deleteTodo(request, pk):
    item = TodoItem.objects.get(id=pk)
    if request.method == "POST":
        item.delete()

    return redirect(reverse("todolist:todo"))

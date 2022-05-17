from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from .models import ToDoItem, Priority

# Create your views here.

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/index.html"
       
class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "title",
        "priority",
    ]

    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        context["title"] = "Create A New Todo Item"
        return context

    def get_success_url(self):
        return reverse("index")
    
class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "title",
        "priority",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["title"] = "Edit Todo Item"
        return context

    def get_success_url(self):
        return reverse("index")
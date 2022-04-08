from django.shortcuts import render
from .forms import *
from .models import Priority
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request, 'todo_app/index.html')


def save_task(request):
    return render(request, 'todo_app/save.html')

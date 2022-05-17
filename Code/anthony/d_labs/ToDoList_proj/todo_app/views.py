from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.


def index(request):

    ps = TodoItem.objects.all()

    context = {
        'form': todoitemform(),
        'ps': ps,
    }

    return render(request, 'todo_app/index.html', context)


def todo(request):
    if request.method == 'POST':
        form = todoitemform(request.POST)
        if form.is_valid():
            form.save()
            form = todoitemform()
    else:
        form = todoitemform()
    return HttpResponseRedirect(reverse('index'), {'form': form})

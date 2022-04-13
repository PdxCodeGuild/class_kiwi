from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from .models import *

def home(request):
    grocery = Grocery.objects.all()
    form = GroceryForm()

    if request.method == "POST":
        form = GroceryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ('/')

    context = {'grocery':grocery, 'form':form}

    return render(request, 'grocery_list/home.html',context)

def add(request, pk):
    grocery = Grocery.objects.get(id=pk)

    form = GroceryForm(instance=grocery)

    if request.method == "POST":
        form = GroceryForm(request.POST, instance=grocery)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'grocery_list/add.html', context)

def delete(request,pk):
    grocery = Grocery.objects.get(id=pk)

    if request.method=="POST":
        grocery.delete()
        return redirect('/')

    context = {'grocery': grocery}
    return render(request, 'grocery_list/delete.html', context)


    
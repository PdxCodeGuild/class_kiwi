from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    form = GroceryForm()
    items = GroceryItem.objects.all()

    if request.method == 'POST':
        form = GroceryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form,
               'items': items}

    return render(request,'grocery_app/index.html', context)


def delete(request, pk):
    item = GroceryItem.objects.get(id=pk)

    context = {'item': item}

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    

    return render(request, 'grocery_app/delete.html', context)


def update(request, pk):
    item = GroceryItem.objects.get(id=pk)
    form = GroceryForm(instance=item)

    context = {'form':form,
               'item': item}
                
    if request.method == 'POST':
        form = GroceryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'grocery_app/update.html', context)



from django.http import HttpResponseRedirect
from django.shortcuts import   render
from django.urls import  reverse
from .views import *
from .forms import *
# Create your views here.



def del_item(request, groceryitem_id):
    groceryitem_id = GroceryItem.objects.get(pk=groceryitem_id)
    groceryitem_id.delete()
    return HttpResponseRedirect(reverse('index'))

def add_item(request):
    if request.method == "POST":
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            groceryitem = GroceryItem()
            groceryitem.completed = form.cleaned_data['completed']
            groceryitem.groceryitem = form.cleaned_data['groceryitem']
            groceryitem.save()
        return HttpResponseRedirect(reverse('index'))
    if request.method == "GET":
        form = GroceryItemForm()

        return render(request, 'index.html', {'form': form})

def update_item(request, groceryitem_id):
    if request.method == "POST":
        form = GroceryItemForm(request.POST)
        
        if form.is_valid():
            groceryitem = GroceryItem()
            print('hello')
            groceryitem.completed = form.cleaned_data['completed']
            groceryitem.completed = not groceryitem.completed 
            groceryitem.completed = GroceryItem.objects.filter(pk=groceryitem_id).update('completed')
            form.save()
        return HttpResponseRedirect(reverse('index'))
    if request.method == "GET":
        
        form = GroceryItemForm()
        return render(request, 'index.html', {'form': form})
    # else:
    #     form = GroceryItemForm()

    #     return render(request, 'index.html', {'form': form})

def index(request):
    if request.method == "GET":
        groceryitems = GroceryItem.objects.all()[::]
    return render(request, 'index.html', {
        'groceryitems': groceryitems,
        'form': GroceryItemForm, }
    )
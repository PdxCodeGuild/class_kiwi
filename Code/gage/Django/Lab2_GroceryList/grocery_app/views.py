from django.shortcuts import redirect, render
from grocery_app.models import GroceryItem
from .models import GroceryItem
from grocery_app.forms import GroceryItemForm 
# Create your views here.

def index(request):
    items = GroceryItem.objects.all()
    form = GroceryItemForm
    if request.method == 'POST':
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/grocery')
    context = {'items': items, 'form': form}
    return render(request, 'grocery_app/index.html', context)

def updateItem(request, pk):
    u_item = GroceryItem.objects.get(id=pk)
    u_form = GroceryItemForm(instance=u_item)
    if request.method == "POST":
        u_form = GroceryItemForm(request.POST, instance=u_item)
        if u_form.is_valid():
            u_form.save()
        return redirect('/grocery')
    context = {'uform': u_form}
    return render(request, 'grocery_app/update.html', context)

def removeItem(request, pk):
    r_item = GroceryItem.objects.get(id=pk)
    if request.method == 'POST':
        r_item.delete()
        return redirect('/grocery')
    context = {'ritem': r_item}
    return render (request, 'grocery_app/remove.html', context)
    
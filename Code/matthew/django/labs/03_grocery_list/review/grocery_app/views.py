from django.shortcuts import render, redirect
from .models import Department,GroceryItem
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    # assinging all items in GroceryItem Model to grocery_list and sort by department
    grocery_list= GroceryItem.objects.all().order_by('department')
    # assigning all items in Department Model to departments and sort by name
    departments= Department.objects.all().order_by('name')
    context= {
        'grocery_list':grocery_list,
        'departments':departments
    }
    return render(request, 'grocery_app/index.html', context)

def add_item(request):
    # calling 'item' from input name="item"
    item_text= request.POST['item']
    department_id= request.POST['department']
    new_item= GroceryItem()
    new_item.item= item_text
    # if department was selected via form
    if department_id:
        # getting the Id for the department that was selected via form
        department= Department.objects.get(id=department_id)
        # assigning new item to department
        new_item.department= department
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete_item(request, item_id):
    grocery_item= GroceryItem.objects.get(id=item_id)
    # reverses boolean value
    grocery_item.completed = not grocery_item.completed
    grocery_item.save()
    return redirect(reverse('grocery_list:index'))

def delete_item(request, item_id):
    grocery_item= GroceryItem.objects.get(id=item_id)
    grocery_item.delete()
    return redirect(reverse('grocery_list:index'))
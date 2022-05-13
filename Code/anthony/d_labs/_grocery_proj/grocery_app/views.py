from django.shortcuts import render
from .import models
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
    grocery_list = models.GroceryItem.objects.all().order_by('department')

    departments = models.Department.objects.all().order_by('name')
    context = {
        'grocery_list': grocery_list,
        'departments': departments,
    }
    return render(request, 'grocery_app/index.html', context)


def add_item(request):
    item_text = request.POST['item']
    department_id = request.POST['department']
    new_item = models.GroceryItem()
    new_item.item = item_text
    if department_id:
        department = models.Department.objects.get(id=department_id)
        new_item.department = department
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .import models


# Create your views here.


def index(request):
    grocery_list = models.GroceryItem.objects.all().order_by('department')
    departments = models.Department.objects.all().order_by('name')
    
    return render(request, 'grocery_list/index.html', {
        'grocery_list': grocery_list,
        'departments': departments
    })
    
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
    
def buy_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.completed = not grocery_item.completed
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))
    
def delete_item(request, item_id):
    grocery_item = models.GroceryItem.objects.get(id=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))
    
    
    
    
    
    
    
    
    
    
    
    
    # items = GroceryItem.objects.filter(user=request.user)
    # database = GroceryItem.objects.all()
    # context = {
    #     'items': items,
    #     # 'database': database
    # }
    # return render(request, 'grocery_list/index.html', context)

# def list(request):
    # if request.method == 'POST':
    #     data = request.POST['items']
    #     user = request.user
    #     grocery_item = GroceryItem()
    #     grocery_item.items = data
    #     grocery_item.save()
    #     context = {
    #         'all': data,
    #         'database': database
    #     }
    #     return render(request, 'grocery_list/items.html', context)
    
        
# def grocery_add(request, grocery_id):
#     item = GroceryItem.objects.get(id=grocery_id)
#     database = GroceryItem.objects.all()
#     item.save()
#     context = {
#         'database': database,
#     }
#     return render(request, 'grocery_list/items.html', context)
    
    
    
    
    
    
    
    
# if request.method == 'POST':
        
#         print(request.POST)

#         description = request.POST["description"]
#         created_date = request.POST["created_date"]
#         completed_date = None
#         completed = False
        
#         new_item = GroceryItem(description = description, created_date = created_date, completed_date = completed_date, completed=completed)

        
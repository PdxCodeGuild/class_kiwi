from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'grocery_app/index.html')
    grocery_list = models.GroceryItem.objects.all().order_by('department')
    departments = models.Department.objects.all().order_by('name')

    return render(request, 'grocery_app/index.html',{
        'grocery_list': grocery_list,
        'departments': departments
    }
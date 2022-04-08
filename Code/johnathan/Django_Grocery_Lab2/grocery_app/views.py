from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import Grocery_Model

def category(request):
    category = Grocery_Model.objects.all()
    context = { 
        'grocery_items': groceryitems
    }
    return render(request,'grocery_app/index.html', context)
# Create your views here.

def grocery_order(request):
    grocery_field = request.POST['grocery_field']
    grocery_model = Grocery_Model(grocery_field=grocery_field)
    grocery_model.save()
    return HttpResponseRedirect(reverse('grocery_app:grocery_view')) 
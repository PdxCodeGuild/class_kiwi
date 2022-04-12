from pickle import NONE
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Category, GroceryItem

def grocery_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    groceryitems = GroceryItem.objects.filter(available = True)
    if category_slug:
        category = get_object_or_404 (Category, slug = category_slug)
        groceryitems = groceryitems.filter(category=category)
        return render(request, 'grocery_app\list.html', {'category': category, 'categories': categories, 'groceryitems': groceryitems})
# Create your views here.

def grocery_details (request, id, slug):
    product= get_object_or_404(GroceryItem, id=id, slug=slug, available=True )
    return render(request, ' grocery_app/index.html', {'groceryitem': groceryitem} )
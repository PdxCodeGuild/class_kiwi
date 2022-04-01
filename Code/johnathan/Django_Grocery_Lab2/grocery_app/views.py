from django.shortcuts import render, get_object_or_404
from shopping_cart.models import Order
from .models import Grocery_Item
# from django.http import HttpResponseRedirect


# def grocery_view(request):
#     groceryitems = Grocery_Model.objects.all()
#     context = { 
#         'grocery_items': groceryitems
#     }
#     return render(request,'grocery_app/index.html', context)
# # Create your views here.

# def grocery_order(request):
#     grocery_field = request.POST['grocery_field']
#     grocery_model = Grocery_Model(grocery_field=grocery_field)
#     grocery_model.save()
#     return HttpResponseRedirect(reverse('grocery_app:grocery_view')) 

def my_shopping_cart(request):
    my_user_profile = Grocery_Item.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_object=True, owner=my_user_profile)
    context = {
        'grocery_order': grocery_order
    }
    return render(request, "profile.html", context)
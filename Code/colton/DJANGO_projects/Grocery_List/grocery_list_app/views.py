from pyexpat import model
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse, reverse_lazy

# from Grocery_List.grocery_list_app.forms import GroceryForm
from .models import Grocery
from django.views.generic.edit import DeleteView, UpdateView
from .forms import *


# Create your views here.
class GroceryDelete(DeleteView):
    model = Grocery
    success_url = reverse_lazy("grocery:create")


class NewItemForm(forms.Form):

    quantity = forms.IntegerField(label="", initial=1)
    text = forms.CharField(label="", max_length=50)


def contact(request):
    return render(request, "grocery_list_app/contact.html")


def about(request):
    return render(request, "grocery_list_app/about.html")


def create(request):
    items = Grocery.objects.all()

    context = {
        "form": NewItemForm(),
        "items": items,
        "check": GroceryForm(),
    }
    return render(request, "grocery_list_app/create.html", context)


# def checkGrocery(request, pk):
#     item = Grocery.objects.get(id=pk)
#     form = GroceryForm(instance=items)

#     if request.method == "POST":
#         item.completed = True
#         form = GroceryForm(request.POST, instane=item)
#         if form.is_valid():
#             form.save()
#         return redirect("/")

#     context = {"form": form}

#     return render(request, "grocery_list_app/create.html", context)
def check_item(request, pk):
    item = Grocery.objects.get(id=pk)
    form = GroceryForm(instance=item)
    if request.method == "POST":
        item.completed = True
        form = GroceryForm(request.POST, instance=item)

        if form.is_valid():
            form.save()

    return redirect(reverse("grocery:create"))


def save_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST)

        if form.is_valid():
            text = form.cleaned_data["text"]
            quantity = form.cleaned_data["quantity"]

            # user = request.user
            grocery = Grocery()
            grocery.item = text
            # grocery.user = user
            grocery.quantity = quantity
            grocery.save()

    return HttpResponseRedirect(reverse("grocery:create"))

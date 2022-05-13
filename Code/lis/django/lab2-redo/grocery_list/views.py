from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .models import GroceryItem


class NewGroceryItemForm(forms.Form):
    text = forms.CharField(label='Add an item to the list', max_length=50,
                           widget=forms.TextInput(attrs={'placeholder': 'apples'}))


def index(request):
    needed = GroceryItem.objects.filter(
        completed=False,
    )
    completed = GroceryItem.objects.filter(
        completed=True,
    )

    return render(request, 'grocery_list/index.html', {
        'form': NewGroceryItemForm(),
        'needed': needed,
        'completed': completed
    })


def save_grocery_item(request):
    if request.method == 'POST':
        form = NewGroceryItemForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            grocery_item = GroceryItem()
            grocery_item.item = text
            grocery_item.save()

    return HttpResponseRedirect('/grocery_list/')


def delete_grocery_item(request, grocery_item):
    if request.method == 'POST':
        item_to_delete = GroceryItem.objects.get(id=grocery_item)
        item_to_delete.delete()

    return HttpResponseRedirect('/grocery_list/')


def update_grocery_item_true(request, grocery_item):
    if request.method == 'POST':
        GroceryItem.objects.filter(id=grocery_item).update(completed=True)

    return HttpResponseRedirect('/grocery_list/')


def update_grocery_item_false(request, grocery_item):
    if request.method == 'POST':
        GroceryItem.objects.filter(id=grocery_item).update(completed=False)

    return HttpResponseRedirect('/grocery_list/')

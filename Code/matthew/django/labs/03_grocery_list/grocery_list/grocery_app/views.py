from django.shortcuts import get_object_or_404, render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import List

class NewItem(forms.Form):
    item= forms.CharField(label='',widget=forms.TextInput(
        attrs={'placeholder': 'Add new item'}), max_length=10)

# Create your views here.
def home(request):
    show_items= List.objects.filter(delete= False).order_by('date')
    context= {
        'new_item': NewItem,
        'show_items': show_items
    }
    
    return render(request, 'grocery_app/index.html', context)

# add new item. Must be logged into a user
def save(request):
    if request.method == "POST":
        form= NewItem(request.POST)
        if form.is_valid():
            text= form.cleaned_data['item']
            # 
            list=List()
            list.new= text
            list.user= request.user
            list.save()
    return HttpResponseRedirect(reverse('home'))

def delete(request, id):
    List.objects.filter(id=id).delete()

           
    return HttpResponseRedirect(reverse('home'))

def edit(request, id):
    item= List.objects.filter(id=id)

    context= {
        'item': item,
    }

    return render(request, 'grocery_app/edit.html', context)

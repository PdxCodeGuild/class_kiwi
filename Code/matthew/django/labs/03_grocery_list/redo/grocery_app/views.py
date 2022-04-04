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

def save(request):
    if request.method == "POST":
        form= NewItem(request.POST)
        if form.is_valid():
            text= form.cleaned_data['item']
            user= request.user
            # 
            list=List()
            list.new= text
            list.user= user
            list.save()
    return HttpResponseRedirect(reverse('home'))

def delete(request, id):
    if request.method == 'GET':
        List.objects.filter(id=id).delete()
        # list= get_object_or_404(List, id=id)
        # list.delete
    return HttpResponseRedirect(reverse('home'))

    
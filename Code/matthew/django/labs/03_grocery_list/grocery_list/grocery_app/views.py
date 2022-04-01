from hashlib import new
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import List

# Create your views here.
class new_list(forms.Form):
    text= forms.CharField(label='',widget=forms.TextInput(
        attrs={'placeholder': 'Add new item'}), max_length=10)


def home(request):
    # folder= List.objects.all().order_by('date')
    folder= List.objects.filter(delete= False).order_by('-date')
    context= {
        "new": new_list(),
        'folder': folder
    }
    return render(request, "grocery_app/index.html", context)

def save(request):
    if request.method == 'POST':
        form= new_list(request.POST)
        if form.is_valid():
            text= form.cleaned_data['text']
            user= request.user

            list= List()
            list.new= text
            list.user= user
            list.save()
    return HttpResponseRedirect(reverse('home'))


from django.shortcuts import render
from django import forms

#new and cool stuff to talk about
from django.http import HttpResponseRedirect
from django.urls import reverse
from numpy import delete
from .models import Cheep


class NewCheepForm(forms.Form):
    text = forms.CharField(label='Cheep your thoughts here', max_length=120, widget=forms.TextInput(attrs={'placeholder': 'Feeling Chirpy?'}))
    #forms.CharField(label='search',widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    
    
# Create your views here.
def index(request):
    #cheeps = Cheep.objects.all().order_by('-date_published')
    cheeps = Cheep.objects.filter(deleted=False).order_by('-date_published')
    
    return render(request, 'chirpy_app/index2.html', {
        'form': NewCheepForm(),
        'cheeps': cheeps
    })
    
def save_cheep(request):
    if request.method == 'POST':
        form = NewCheepForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            user = request.user
            
            cheep = Cheep() 
            cheep.chirp = text
            cheep.user = user
            cheep.save()
            
    return HttpResponseRedirect(reverse('index2'))


'''
def index(request):
    #cheeps = Cheep.objects.all().order_by('-date_published')
    cheeps = Cheep.objects.filter(deleted=False).order_by('-date_published')
    
    return render(request, 'chirpy_app/index2.html', {
        'form': NewCheepForm(),
        'cheeps': cheeps
    })




'''
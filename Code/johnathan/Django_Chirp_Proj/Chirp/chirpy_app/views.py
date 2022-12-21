from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cheep


class NewCheepForm(forms.Form):
    text = forms.CharField(label='Cheep your thoughts here', )

# Create your views here.
def index(request):
    return render(request, 'chirpy_app/index.html', {
        'form': NewCheepForm()
    })

def save_cheep(request):
     if request.method == 'Post':
        form = NewCheepForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text'] 
            user = request.user

            cheep = Cheep()
            cheep.chirp = text
            cheep.user = user
            cheep.save()

    return HttpResponseRedirect(reverse('index'))

    # return render(request, 'chirpy_app/index.html', {
    #     'form':NewCheepForm()
    # })
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cheep


# Classes
class NewCheepForm(forms.Form): # Creates a form (so we don't have to code a full form in html)
    text = forms.CharField(label='Post a Cheep!', max_length=120)


# Create your views here.
def index(request):
    cheeps = Cheep.objects.filter(deleted=False).order_by('-date_published')
    return render(request, "chirpy_app/index1.html", {'form': NewCheepForm(), 'cheeps': cheeps})

def save_cheep(request):
    if request.method == 'post':
        form = NewCheepForm(request.post) # '(request.post) refers to the sent form data
        if form.is_valid():
            text = form.cleaned_data['text'] # brings submitted text data from form
            user = request.user # targets logged in user

            cheep = Cheep()
            cheep.chirp = text
            cheep.user = user
            cheep.save()
    return HttpResponseRedirect(reverse('chirpy:index1')) # reverse targets the path name='index' in the urls.py file
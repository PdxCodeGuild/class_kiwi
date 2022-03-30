
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Cheep
# Create your views here.


class NewCheepForm(forms.Form):
    text1 = forms.CharField(label='Cheep your thoughts here', widget=forms.TextInput(
        attrs={'placeholder': 'Cheep away'}), max_length=120)


def index(request):

    return render(request, 'chirpy_app/index.html', {
        'form': NewCheepForm(),
    })


def save_cheep(request):
    if request.method == 'POST':
        form = NewCheepForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text1']
            user = request.user
            # Linking Cheep() in models.py and automatically updating chirp and user

            cheep = Cheep()  # Ex: cheep.date_published
            cheep.chirp = text
            cheep.user = user
            cheep.save()

    return HttpResponseRedirect(reverse('index'))

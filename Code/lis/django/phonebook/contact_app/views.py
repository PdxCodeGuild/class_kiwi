from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, reverse
from .models import *


# Create your views here.
def home_page(request):
    return render(request, 'contact_app/index.html')


def all_contacts(request):
    contacts = Contact.objects.all()

    context = {
        'contacts': contacts
    }

    return render(request, 'contact_app/all_contacts.html', context)


def save_contact(request):
    contact = Contact()
    form = request.POST

    if request.POST:
        #print(request.POST, 'checking.............')
        contact.first_name = form['first_name']
        contact.last_name = form['last_name']
        contact.phone_number = form['phone_number']
        contact.email = form['email']
        contact.address = form['address']
        if form.get('is_cool') == 'on':
            contact.is_cool = True
        else:
            contact.is_cool = False

        contact.save()

    return HttpResponseRedirect(reverse('contacts:all_contacts'))


def search_contact(request):
    name = request.POST['first_name']

    if name:
        contact = Contact.objects.filter(first_name__iexact=name)
    else:
        contact = ''

    return HttpResponse(contact)

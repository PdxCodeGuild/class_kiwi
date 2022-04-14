from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def home_page(request):
    return render(request, 'contactsapp/index.html')


def all_contacts(request):
    contacts = Contact.objects.all()

    contact = {
        'contacts': contacts
    }
    return render(request, 'contactsapp/all_contacts.html', contact)


def save_contact(request):
    contact = Contact()
    form = request.POST

    if request.POST:

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

    return HttpResponseRedirect(reverse('contactsapp:all_contacts'))


def search_contact(request):
    name = request.POST['first_name']
    if name:
        contact = Contact.objects.filter(first_name=name)

    else:
        contact = ''

    return HttpResponse(contact)


from multiprocessing import context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *

# Create your views here.
def home_page(request):

    return render(request, 'contact_app/index.html')

def all_contacts(request):
    contacts= Contact.objects.all()
    context= {
        'contacts':contacts
    }
    return render(request, 'contact_app/all_contacts.html', context)

def save_contact(request):
    # print(request.POST, 'checking form data')
    # return HttpResponse('Form submitted')
    contact= Contact()
    form= request.POST
    # contact.first_name updated by name="first_name" in index.html
    contact.first_name= form['first_name']
    contact.last_name= form['last_name']
    contact.phone_number= form['phone_number']
    contact.email= form['email']
    contact.address= form['address']
    # only works if box remains unchecked
    # if form['fav'] == 'on':
    if form.get('fav') == 'on':
        contact.fav = True
    else:
        contact.fav = False
    contact.save()
    return redirect(reverse('contacts:all'))

def search_contact(request):
    # stuff= request.POST['first_name']
    # return HttpResponse(stuff)
    name= request.POST['first_name']
    # if anything was typed in search box: if name has a value
    if name:
        # search is CASE SeNsITVe
        # contacts= Contact.objects.all().filter(first_name=name)
        # search is not longer case sensitive
        # filter= Contact.objects.filter(first_name__iexact=name)
        # if not Contact.objects.filter(first_name__iexact=name) == None:

        filter= Contact.objects.filter(first_name__iexact=name)
    context= {
        # 'contacts':contacts,
        'filter':filter
    }
    # return HttpResponse(filter)
    # return HttpResponseRedirect(reverse('contacts:home'), context)
    return render(request, 'contact_app/index.html', context)



from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):

    commodity = Item.objects.all().order_by('section')
    stores = StoreDepartment.objects.all().order_by('store')

    context = {
        'commodity':commodity,
        'stores':stores
    }

    return render(request, 'app_groc/index.html', context)

def add_prod(request):
    produce = request.POST['item']
    section_id = request.POST['section']
    added_prod = Item()

    added_prod.item = produce 

    if section_id:
        section = StoreDepartment.objects.get(id=section_id)
        added_prod.section = section
    
    added_prod.save()

    return HttpResponseRedirect(reverse('app_groc:index'))

def complete_prod(request,prod_id):

    produce = Item.objects.get(id=prod_id)
    produce.done = not produce.done 
    produce.save()

    return HttpResponseRedirect(reverse('app_groc:index'))

def delete_prod(request, prod_id):
    produce = Item.objects.get(id=prod_id)
    produce.delete()

    return HttpResponseRedirect(reverse('app_groc:index'))

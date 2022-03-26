from django.shortcuts import render
from django.http import HttpResponse

#import 
from .models import Kiwi

# Create your views here.
def home(request):
    
    #getting all the data from model
    results = Kiwi.objects.all()
    
    context = {
        'results' : results
    }
    
    #return HttpResponse('<h3>Testing testing page</h3>')
    return render(request, 'index.html', context )
    

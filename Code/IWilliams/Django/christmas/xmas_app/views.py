from django.shortcuts import render
import datetime as dt
# Create your views here.
def index(request):
    now = dt.datetime.now()
    
    context = {
        'xmas' : now.month == 12 and now.day == 25
    }    
    
    return render(request, 'xmas_app/index.html', context)
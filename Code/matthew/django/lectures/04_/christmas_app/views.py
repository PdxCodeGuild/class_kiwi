from multiprocessing import context
from django.shortcuts import render
import datetime as dt

# Create your views here.


def home(request):
    now = dt.datetime.now()

    print(now)

    context = {
        'now': now,
        'xmas': now.month == 12 and now.day == 25
    }

    return render(request, 'christmas_app/index.html', context)

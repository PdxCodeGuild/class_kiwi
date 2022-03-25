from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def unitcon(request):
    return render(request, 'redoapp/unitcon.html')


def result(request):
    conversion = request.POST

    units_to_convert = conversion['convert']
    distance_to_convert = conversion['amount']
    meters_to_units = conversion['converted']
    distance_to_convert = int(distance_to_convert)

    distances = {'feet': 0.3048, 'miles': 1609.34, 'meters': 1.0,
                 'kilometers': 1000, 'yards': 0.9144, 'inches': 0.0254}
    # convert the meters into the desired second unit and print results
    units_to_meters = distance_to_convert * distances.get(units_to_convert)
    converted_units = units_to_meters / distances.get(meters_to_units)
    converted_units = round(converted_units, 3)

    context = {'converted_units': converted_units,
               'meters_to_units': meters_to_units,
               'units_to_convert': units_to_convert,
               'distance_to_convert': distance_to_convert
               }

    return render(request, 'redoapp/result.html', context)

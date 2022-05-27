
from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'unit_converter_app/index.html')


# request.POST is grabbing the information inside of the from submission
def forms(request):
    form_post = request.POST

    #EXAMPLE: distance=form_post['distance']

    distance = form_post['distance']
    units = form_post['user_units']
    units_to_convert = form_post['conversion_units']

    def feet_to_meters(x):
        converted_ft = float(x) * .3048
        return converted_ft

    def mile_to_meters(x):
        converted_mi = float(x) * 1609.34
        return converted_mi

    def km_to_meters(x):
        converted_km = float(x) * 1000
        return converted_km

    def meters_to_feet(x):
        converted_ft = float(x) * 3.28084
        return converted_ft

    def meters_to_mile(x):
        converted_mi = float(x) * .000621371
        return converted_mi

    def meters_to_km(x):
        converted_km = float(x) * .001
        return converted_km

    if units.lower() == 'mi' and units_to_convert.lower() == 'km':
        converted_output = meters_to_km(mile_to_meters(distance))
        print(f'\n {distance}mi is {converted_output}km')

    elif units.lower() == 'mi' and units_to_convert.lower() == 'm':
        converted_output = mile_to_meters(distance)
        print(f'\n {distance}mi is {converted_output}m')

    elif units.lower() == 'mi' and units_to_convert.lower() == 'ft':
        converted_output = meters_to_feet(mile_to_meters(distance))
        print(f'\n {distance}mi is {converted_output}ft')

    elif units.lower() == 'km' and units_to_convert.lower() == 'mi':
        converted_output = meters_to_mile(km_to_meters(distance))
        print(f'\n {distance}km is {converted_output}mi')

    elif units.lower() == 'km' and units_to_convert.lower() == 'm':
        converted_output = km_to_meters(distance)
        print(f'\n {distance}km is {converted_output}m')

    elif units.lower() == 'km' and units_to_convert.lower() == 'ft':
        converted_output = meters_to_feet(km_to_meters(distance))
        print(f'\n {distance}km is {converted_output}ft')

    elif units.lower() == 'ft' and units_to_convert.lower() == 'mi':
        converted_output = mile_to_meters(feet_to_meters(distance))
        print(f'\n {distance}ft is {converted_output}mi')

    elif units.lower() == 'ft' and units_to_convert.lower() == 'm':
        converted_output = feet_to_meters(distance)
        print(f'\n {distance}ft is {converted_output}m')

    elif units.lower() == 'ft' and units_to_convert.lower() == 'km':
        converted_output = meters_to_km(feet_to_meters(distance))
        print(f'\n {distance}mi is {converted_output}ft')

    elif units.lower() == 'm' and units_to_convert.lower() == 'ft':
        converted_output = meters_to_feet(distance)
        print(f'\n {distance}km is {converted_output}ft')

    elif units.lower() == 'm' and units_to_convert.lower() == 'mi':
        converted_output = meters_to_mile(distance)
        print(f'\n {distance}ft is {converted_output}mi')

    elif units.lower() == 'm' and units_to_convert.lower() == 'km':
        converted_output = meters_to_km
        print(f'\n {distance}mi is {converted_output}ft')

    context = {
        'distance': distance,
        'converted_output': converted_output,
        'units': units,
        'units_to_convert': units_to_convert,
    }

    return render(request, 'unit_converter_app/result.html', context)

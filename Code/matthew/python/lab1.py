'''
Lab 1
Unit Converter
'''
# def for version 1 -3         !!!!!!!!! <---------

# def meters_to_feet(x):
#     converted_ft = x * .3048         #### all function names are backwards meters_to_feet is feet_to_meters.. ect
#     return converted_ft

# # print(meters_to_feet(10))

# def meters_to_mile(x):
#     converted_mi = x * 1609.34
#     return converted_mi

# def meters_to_km(x):
#     converted_km = x * 1000
#     return converted_km

# def meters_to_yard(x):
#     converted_yd = x * .9144
#     return converted_yd

# def meters_to_inch(x):
#     converted_in = x * .0254
#     return converted_in



# print(meters_to_feet(10))   # 3.048

# --- Version 1
''' 

feet = int(input("enter the distance you wish to convert to meters: "))  
print(f'\n {feet}ft is {meters_to_feet(feet)}m')          # 10ft is [3.048]m  # need to remove brackets
'''
# --- Version 2

'''

distance = int(input('Enter the total distance: '))
units = input('Enter the units you wish to convert to meters (mi, km, ft) ')
converted_output = []

if units.lower() == 'mi':
    converted_output = meters_to_mile(distance)
    print(f'\n {distance}mi is {converted_output}m')
elif units.lower() == 'km':
    converted_output = meters_to_km(distance)
    print(f'\n {distance}km is {converted_output}m')
elif units.lower() == 'ft':
    converted_output = meters_to_feet(distance)
    print(f'\n {distance}ft is {converted_output}m')
else: 
    print('Did not reconize input')

'''    

# --- Version 3

'''

# distance = int(input('Enter the total distance: '))
# units = input('Enter the units you wish to convert to meters (mi, km, ft, in or yd) ')
# converted_output = []

# if units.lower() == 'mi':
#     converted_output = meters_to_mile(distance)
#     print(f'\n {distance}mi is {converted_output}m')
# elif units.lower() == 'km':
#     converted_output = meters_to_km(distance)
#     print(f'\n {distance}km is {converted_output}m')
# elif units.lower() == 'ft':
#     converted_output = meters_to_feet(distance)
#     print(f'\n {distance}ft is {converted_output}m')
# elif units.lower() == 'in':
#     converted_output = meters_to_inch(distance)
#     print(f'\n {distance}in is {converted_output}m')
# elif units.lower() == 'yd':
#     converted_output = meters_to_yard(distance)
#     print(f'\n {distance}yd is {converted_output}m')

'''

# --- Version 4

def feet_to_meters(x):
    converted_ft = x * .3048         
    return converted_ft  

def mile_to_meters(x):
    converted_mi = x * 1609.34
    return converted_mi

def km_to_meters(x):
    converted_km = x * 1000
    return converted_km

def meters_to_feet(x):
    converted_ft = x * 3.28084         
    return converted_ft  

def meters_to_mile(x):
    converted_mi = x * .000621371
    return converted_mi

def meters_to_km(x):
    converted_km = x * .001
    return converted_km


distance = int(input('Enter the total distance: '))
units = input('Enter the units you are using (mi, km, ft, m) ')
units_to_convert = input('Enter the units you wish to convert to (mi, km, ft, m) ')

if units.lower() == 'mi'and units_to_convert.lower() == 'km':  
    converted_output = meters_to_km(mile_to_meters(distance))
    print(f'\n {distance}mi is {converted_output}km')

elif units.lower() == 'mi'and units_to_convert.lower() == 'm':  
    converted_output = mile_to_meters(distance)
    print(f'\n {distance}mi is {converted_output}m')

elif units.lower() == 'mi'and units_to_convert.lower() == 'ft':  
    converted_output = meters_to_feet(mile_to_meters(distance))
    print(f'\n {distance}mi is {converted_output}ft')

elif units.lower() == 'km'and units_to_convert.lower() == 'mi':  
    converted_output = meters_to_mile(km_to_meters(distance))
    print(f'\n {distance}km is {converted_output}mi')

elif units.lower() == 'km'and units_to_convert.lower() == 'm':  
    converted_output = km_to_meters(distance)
    print(f'\n {distance}km is {converted_output}m')

elif units.lower() == 'km'and units_to_convert.lower() == 'ft': 
    converted_output = meters_to_feet(km_to_meters(distance))
    print(f'\n {distance}km is {converted_output}ft')

elif units.lower() == 'ft'and units_to_convert.lower() == 'mi':  
    converted_output = mile_to_meters(feet_to_meters(distance))
    print(f'\n {distance}ft is {converted_output}mi')

elif units.lower() == 'ft'and units_to_convert.lower() == 'm':  
    converted_output = feet_to_meters(distance)
    print(f'\n {distance}ft is {converted_output}m')

elif units.lower() == 'ft'and units_to_convert.lower() == 'km':  
    converted_output = meters_to_km(feet_to_meters(distance))
    print(f'\n {distance}mi is {converted_output}ft')

elif units.lower() == 'm'and units_to_convert.lower() == 'ft':  
    converted_output = meters_to_feet(distance)
    print(f'\n {distance}km is {converted_output}ft')

elif units.lower() == 'm'and units_to_convert.lower() == 'mi':  
    converted_output = meters_to_mile(distance)
    print(f'\n {distance}ft is {converted_output}mi')

elif units.lower() == 'm'and units_to_convert.lower() == 'km':  
    converted_output = meters_to_km
    print(f'\n {distance}mi is {converted_output}ft')





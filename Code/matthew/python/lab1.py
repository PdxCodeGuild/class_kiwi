'''
Lab 1
Unit Converter
'''

def meters_to_feet(x):
    converted_ft = []
    converted_ft.append(x * .30480)
    return converted_ft

def meters_to_mile(x):
    converted_mi = []
    converted_mi.append(x * 1609.34)
    return converted_mi

def meters_to_km(x):
    converted_km = []
    converted_km.append(x * 1000)
    return converted_km

def meters_to_yard(x):
    converted_yd = []
    converted_yd.append(x * .9144)
    return converted_yd

def meters_to_inch(x):
    converted_in = []
    converted_in.append(x * .0254)
    return converted_in

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

distance = int(input('Enter the total distance: '))
units = input('Enter the units you wish to convert to meters (mi, km, ft, in or yd) ')
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
elif units.lower() == 'in':
    converted_output = meters_to_inch(distance)
    print(f'\n {distance}in is {converted_output}m')
elif units.lower() == 'yd':
    converted_output = meters_to_yard(distance)
    print(f'\n {distance}yd is {converted_output}m')








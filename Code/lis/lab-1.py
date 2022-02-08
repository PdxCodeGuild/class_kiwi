# Lab 01

# *** Version 1 ***


# create dictionary
conversion = {
    'ft': 0.3048
}
# get user inputs
user_input = int(input('What is the distance in feet? '))

# convert
convert_units = user_input * conversion['ft'] 

# output statement
print(f'{user_input} ft is {round(convert_units, 4)} m')



# *** Version 2 ***

'''
# create dictionary
conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

while True:
    # get user inputs
    distance = int(input('What is the distance? '))
    units = input('What are the units (choose: ft, mi, m, or km)? ').lower()

    if units not in conversion:
        print(f'{units} is an invalid input')
        units = input('What are the units (choose: ft, mi, m, or km)? ').lower()

    # get dictionary item
    unit = conversion[units]

    # convert
    convert_units = distance * unit

    # output statement
    print(f'{distance} {units} is {round(convert_units, 4)} m') 
    break 
'''


# *** Version 3 ***

'''
# create dictionary
conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

# get user inputs
distance = int(input('What is the distance? '))
units = input('What are the units (choose: ft, mi, m, km, yd, or in)? ').lower()

# validate for units user input 
if units not in conversion:
    print(f'{units} is an invalid input')
    units = input('What are the units (choose: ft, mi, m, km, yd, or in)? ').lower()

# get dictionary item
unit = conversion[units]

# convert
convert_units = distance * unit

# output statement
print(f'{distance} {units} is {round(convert_units, 4)} m')  
'''

 # *** Version 4 ***


'''
# create dictionary
conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

# get user inputs
distance = int(input('What is the distance? '))
input_unit = input('What are the input units (choose: ft, mi, m, or km)? ').lower()

# validate for user input units 
if input_unit not in conversion:
    print(f'{input_unit} is an invalid input')
    input_unit = input('What are the input units (choose: ft, mi, m, or km)? ').lower()

# get user output
output_unit = input('What are the output units (choose: ft, mi, m, or km)? ').lower()

# validate for user output units
if output_unit not in conversion:
    print(f'{output_unit} is an invalid input')
    output_unit = input('What are the output units (choose: ft, mi, m, or km)? ').lower()

# get dictionary item
unit_input = conversion[input_unit]

# convert to meters
convert_meters = distance * unit_input

# convert meters to output unit
convert_output = convert_meters / conversion[output_unit]

# output statement
print(f'{distance} {input_unit} is {round(convert_output, 7)} {output_unit}')  
'''
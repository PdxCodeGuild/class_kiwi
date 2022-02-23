# Lab 1: Version 4

# User's inputs will determine distance and which units are being converted
dist = float(input('What is the distance?: '))
unit_in = input('What are the input units? (ft, mi, m, km): ').lower()
unit_out = input('What are the outpu units? (ft, mi, m, km): ').lower()

# two dictionaries displaying units as the key with their respective conversion to and from m
units_to_m = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

"""
For purpose of lab showing 'from_m' dictionary with described matrix, 
but could have kept single dictionary and 
in conversion function divided 1 by units_to_m[unit_in]
this would have less changes to code
"""
units_from_m = {
    'ft': 1/0.3048,
    'mi': 1/1609.34,
    'm': 1,
    'km': 1/1000
}

# function calculating the arguments needed for conversion
# input unit to m then to selected output
def conversion(dist, unit_in, unit_out):  
    to_m = dist * units_to_m[unit_in]
    from_m = to_m * units_from_m[unit_out]
    return from_m

# Display user's inputs and conversion
if unit_in == unit_out:
    print(f'No conversion is necessary. {dist} {unit_in} is {dist} {unit_out}')

else:
    print(f' {dist} {unit_in} is {round(conversion(dist, unit_in, unit_out), 7)} {unit_out}')
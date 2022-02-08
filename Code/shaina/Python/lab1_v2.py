# Lab 1: Version 2

# User's inputs will determine distance and unit
dist = float(input('What is the distance?: '))
unit = input('What are the units? (ft, mi, m, km): ').lower()

# dictionary displaying units as the key with their respective conversion to m
units_to_m = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

# function calculating the arguments needed for conversion (distance * m)
def conversion(dist, unit):
    to_m = dist * units_to_m[unit]
    return to_m

# Display user's inputs and conversion
print(f' {dist} {unit} is {round(conversion(dist, unit), 4)} m')
# Lab 01 - Unit Converter - Version 3 - Working

# Ask the user for the distance
dist = float(input('What is the distance? '))

# Maths
dist_f = dist * 0.3048
dist_mi = dist * 1609.34
dist_m = dist
dist_km = dist * 1000
dist_yd = dist * 0.9144
dist_in = dist * 0.0254


# Ask user for the unit of measurement
unit = input('What are the units? (feet = f, miles = mi, meters = m, kilometers = km, yards = yd, inches = in) ')

# Output appropriate conversion

if unit == 'f':
    print(dist, 'feet is', dist_f, 'm')
elif unit == 'mi':
    print(dist, 'miles is', dist_mi, 'm')
elif unit == 'm':
    print(dist, 'm is', dist_m, 'm')
elif unit == 'km':
    print(dist, 'km is', dist_km, 'm')
elif unit == 'yd':
    print(dist, 'yd is', dist_yd, 'm')
elif unit == 'in':
    print(dist, 'in is', dist_in, 'm')
else:
    print('Invalid units')
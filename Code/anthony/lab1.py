
# Lab 1: Unit Converter

# ask for number of  feet
# feet = float(input("Please enter the number of feet.: "))
# meters conversion
# meters = feet * 0.3048
# Output
# print(f"{feet} ft is {round(meters,2)} m.")

# Version 2
# ask for distance
distance = int(input("What is the distance? "))
# ask for unit
units = input("What are the units (ft, mi, m, km, yard, inch)?: ")

# if statement to determine conversion
if units == "ft":
    conversion = distance * 0.3048
elif units == "mi":
    conversion = distance * 1690.34
elif units == "m":
    conversion = distance
elif units == "km":
    conversion = distance * 1000
elif units == "yard":
    conversion = distance * 0.9144
else:
    conversion = distance * 0.254

# output
print(f"{distance} {units} is {conversion} m.")

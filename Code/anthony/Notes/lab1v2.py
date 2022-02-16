###  Lab 1 Version 2 Practice  ###
################################
##                            ##
## Lab 1.2: Unit Converter      ##
##   Author: Anthony Bilie    ##
##   Date: 2/13/2022          ##
##                            ##
################################

# Added Version 3
"""
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
"""

unit_dict = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meter": 1,
    "kilometer": 160934,
    "yard": 0.9144,
    "inch": 0.0254
}

meters_conv_dict = {
    "feet": 3.28,
    "miles": 0.00062137,
    "meter": 1,
    "kilometer": .001
}
# Ask user for distance
distance = input("What is the distance? ")
# convert distance from string to interger
distance = int(distance)


# ask user for units
unit = input(f"What are the input units? {' '.join(unit_dict.keys())} ")
# ask for ending units
ending_unit = input(f"What are the output units? {' '.join(unit_dict.keys())}")

# conversions
conversion = distance * unit_dict[unit]
# 2nd converstion to convert output unit
conversion2 = conversion * meters_conv_dict[ending_unit]
# print outcome
print(f"{distance} {unit} is {conversion2} {ending_unit}.")

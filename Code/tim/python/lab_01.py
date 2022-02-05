"""Project: Signature
Author: Timothy Hampton
Email: Hampton12101@gmail.com
Date: Feb 03 2022"""

# Ask the user for the number for Feet

# Print out the equivalent distance in meters.

# 1 Foot is 0.3048 M 

# convert by multiplying the input by 0.3048

######### VERSION 1 #########################

# user_input = input("What is the distance in feet? ")

# user_input = float(user_input)


# print(f"{user_input} is {user_input * .03048} meters.")

########### Version 2 ################################

# We will do the same but we will also allow the user to enter units. 

# These units are Feet | Miles | Meters | Kilometers

# Their conversions are 1 ft is 0.3048 m | 1 mi is 1609.34 m 
# 1 m is 1 m | 1 km is 1000 m

distance = input("Please enter the distance you would like to convert to meters: ")

distance = float(distance)

units = input("Please enter the unit as, ft, mi, m, km, yard, or inches: ").lower()


if units == "ft":
    print(f"{distance}{units} is {distance * .03048} meters.")

elif units == "mi":
    print(f"{distance}{units} is {distance * 1609.34} meters.")

elif units == "m":
    print(f"{distance}{units} is {distance} meters.")

elif units == "km":
    print(f"{distance}{units} is {distance * 1000} meters.")



################# Version 3 ##############

# Add support for Yards and Inches

# 1 Yard is 0.9144 m | 1 inch is 0.0254 m

elif units == "yard" or units == "yd":
    print(f"{distance}{units} is {distance * 0.9144} meters.")
elif units == "inches" or units == "in":
    print(f"{distance}{units} is {distance * 0.0254} meters.")
else:
    print("Please follow instructions.")
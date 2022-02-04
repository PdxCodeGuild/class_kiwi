# Version 1
# asking user for number of feet, then converting to meters
user_input = input("Please provide a distance in feet: ")
feet_to_meter = int(user_input) * .3048
print(f"You inputed {user_input} which will convert to {round(feet_to_meter, 2)} meters")

# Version 2
# asking user for distance to convert and unit to convert to
user_input = input("Please provide a distance to convert: ")
user_unit = input("Please select a unit of measure: ").lower()

#performing conversion based on unit selected
if user_unit == "ft" or user_unit == "feet":
    ft_to_meter = int(user_input) * .3048
    print(f"You inputed {user_input} feet which will convert to {round(feet_to_meter, 2)} meters")
elif user_unit == "mi" or user_unit == "miles":
    mi_to_meter = int(user_input) * 1609.34
    print(f"You inputed {user_input} mile(s) which will convert to {round(mi_to_meter, 2)} meters")
elif user_unit == "m" or user_unit == "meter":
    print(f"You inputed {user_input} meter(s) which will convert to {user_input} meters")
elif user_unit == "km" or user_unit == "kilometer":
    km_to_meter = int(user_input) * 1000
    print(f"You inputed {user_input} kilometer(s) which will convert to {round(km_to_meter, 2)} meters")
else:
    print("Incorrect unit of measure. Please select a proper unit of measure(ft, mi, m, km)")
    
# Version 3
# including yard and inch to possible units of conversion
if user_unit == "yd" or user_unit == "yard":
    yd_to_meter = int(user_input) * .9144
    print(f"You inputed {user_input} yard(s) which will convert to {round(yd_to_meter, 2)} meters")
elif user_unit == "in" or user_unit == "inch":
    in_to_meter = int(user_input) * .0254
    print(f"You inputed {user_input} inch(es) which will convert to {round(in_to_meter, 2)} meters")
"""
# Version 4 - Optional
user_input = input("Please provide a distance to convert: ")
to_unit = input("Please select a starting unit of measure: ").lower()
from_unit = input("Please provide an ending unit of measure to convert to: ").lower()
if from_unit == "ft" or from_unit == "feet" and to_unit == "mi" or to_unit == "miles":
    ft_to_meter = int(user_input) * .3048
    miles_to_feet = ft_to_meter * 1609.344
    print(f"Converting {user_input} {to_unit} to {from_unit} is {round(miles_to_feet, 2)} feet")
else:
    print("try again")
"""
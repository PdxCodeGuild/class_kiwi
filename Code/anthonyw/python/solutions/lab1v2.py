
# Version 2
# Allow the user to also enter the units. 
# Then depending on the units, convert the distance into meters. 
# The units we'll allow are feet, miles, meters, and kilometers.

# Add support for yards, and inches.

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m

# Define conversion rates as a dictionary
# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
conversion_rates = {
    "feet": .3048,
    "miles": 1609.34,
    "meter": 1,
    "kilometer": 1000,
    "yard": .9144,
    "inch": .0254
}

# Function for converting distance to meters
def unit_converter(unit: str, distance: float) -> float:
    '''Takes in a unit and a distance and converts to meters'''
    # 'feet', 12 -> 
    #  'yards' == .3048
    if unit in conversion_rates:
        new_distance = conversion_rates[unit] * distance
    else:
        new_distance = f"Please enter valid unit. {', '.join(conversion_rates.keys())}"
    return new_distance

# Get distance and unit from user
user_input = input(f"Please enter in a unit of measure {', '.join(conversion_rates.keys())}: ")
user_distance = float(input(f"Please enter the number of {user_input}: "))

# Convert input to meters
output = unit_converter(user_input, user_distance)

# Output results
print(output)
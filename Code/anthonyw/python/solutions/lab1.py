

# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. 
# Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
# Below is some sample input/output.


# Define conversion rate for feet to meters
conversion = .3048

# Ask the user for distance in feet
feet = int(input("Please enter distance in feet: "))

# Convert feet to meters
converted_feet = conversion * feet

# Display result
print(f"{feet} ft is {converted_feet:.4f} m")


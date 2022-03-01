# Lab 01 - Unit Converter - Version 1 - Working

# Ask user to input distance in feet, use float as inout because of the math
feet = float(input('What is the distance in feet? '))

# Multiply input by 0.3048
meters = feet * 0.3048

# Output the answer
print(feet, 'ft is equal to', meters, 'meters')
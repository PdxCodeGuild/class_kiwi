# Lab 1: Version 1

# Take user's input to get distance
user = float(input('What is the distance in feet?: '))

# Display conversion by multiplying the .3048 m in ft
print(f'{user} ft is {round(user * .3048, 4)} m')
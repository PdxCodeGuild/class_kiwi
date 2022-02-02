# Colton Tatum
# Class_Kiwi
# Lab 1: Unit Converter



import time # imports time module

conversions= {
    ### This dictionary converts keys into meter lengths ###
    "feet": .3048,
    "meters": 1,
    "kilometers": 1000,
    "miles": 1609.34,
    "yards": .9144,
    "inches": .0254
}


# Version 1
# Gets user's value in feet, and returns value converted to meters
while True:
    try:
        user_int = float(input("How many feet would you like to convert to meters?  "))
        print(f"[{user_int}] feet is ", conversions["feet"] * user_int," meters")
        time.sleep(3)
        break
    except ValueError:
        continue

# Version 2, 3, 4
# Unit Converter allows user to input desired unit and distance to be converted to meters

while True:
    user_input = input("What unit would you like to convert to meters?  ")
    if user_input in conversions:
        try:
            user_int = float(input(f"How many {user_input}? "  ))
            print(f"[{user_int}]{user_input} is ", conversions[user_input] * user_int," meters. ")
            time.sleep(3)
            break

        except ValueError:
            continue
        
    if user_input not in conversions:
        continue


   



time.sleep(5)

user_distance = int(input("Distance length?:  "))
user_units = input("What are the units?:  ")

print(f"{user_distance} {user_units} equals ", conversions[user_units] * user_distance, " meters")
time.sleep(5)





user_distance = int(input("Distance length?:  "))
user_units = input("What are the units?:  ")
user_convert = input("What unit would you like to convert to?:  ")

conversion_1 = conversions[user_units] * user_distance / conversions[user_convert]
print(f"{user_distance} {user_units} equals ", conversion_1 ,f" {user_convert}")

time.sleep(5)


'''         +-+#^#+--+#^#+--+#^#+-+             
            Project: Unit Converter               ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/2/22                     ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''


import time # imports time module

conversions= {
    ### Key values are conversion lengths to convert key to meter lengths ###
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
        # Compares user input to dict keys, and takes value from 'feet' key and multiplies it to user defined lenght
        time.sleep(1) # Pauses code for () second(s)
        break
    
    except ValueError: # Will repeat loop if user_int is not a float
        continue

# Version 2, 3
# Unit Converter allows user to input desired unit and distance to be converted to meters
while True:
    print(conversions.keys()) # Prints usable keys for user to see
    user_input = input("What unit would you like to convert to meters?  ").lower().strip()
    if user_input in conversions: # Looks for user_input in conversions keys
        
        try:
            user_int = float(input(f"How many {user_input}? "  ))
            print(f"[{user_int}]{user_input} is ", conversions[user_input] * user_int," meters. ")
            time.sleep(1)
            break
        
        except ValueError: # Will repeat loop if user_input is not a float
            print("Enter valid input")
            continue
        
    elif user_input not in conversions: # Repeats loop if user_input is not a key in conversions dicitonary
        continue
    

   
# Version 4
# Unit Converter allows user to input desired unit and distance to be converted to desired unit

while True:
    
    try:
        user_int = float(input("What is the distance length of the unit you need to convert?:  "))
    
        while True:
            print(conversions.keys()) # prints dictionary keys for user to see
            user_input = input("What are the units?:  ").lower().strip()
            if user_input not in conversions: # if user_input isn't a dictionary key then repeat loop
                continue
            
            elif user_input in conversions: # if user_input is a dictionary key move to next line
    
                while True:
                    print(conversions.keys()) # print keys for user to see
                    user_convert = input("What unit would you like to convert to?:  ").lower().strip()
                    if user_convert not in conversions: # if user_convert is not in a key in conversions repeat loop
                        continue
                    
                    elif user_convert in conversions: # if user_convert is key in conversions dict move to next line
                        # secect key within conversions dict using user_input, multiply that value by # 
                        # user_int divided by conversions dict key value selected by user_convert     #
                        conversion_1 = conversions[user_input] * user_int / conversions[user_convert] 
                        print(f"{user_int} {user_input} equals ", conversion_1 ,f" {user_convert}")
                        time.sleep(2)
                        break
            
            break
       
        break

    except ValueError: # If user_int is not a valid float it will repeat loop
        print("Please enter valid input")
        continue


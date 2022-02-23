# Unit Converter - Version 1
#distance_to_convert = float(input('Enter the amount of feet to convert to meters: '))
#converted_distance = distance_to_convert * 0.3048

#print(f'{distance_to_convert} feet equals {converted_distance:.3f} meters.')




# Unit Converter - Version 2

#distances = {'feet': 0.3048, 'miles': 1609.34, 'meters': 1.0, 'kilometers': 1000}

#print('Welcome to the unit converter!')
#print(f'This program can convert: feet, miles, meters, and kilometers.')

#def main():

#    while True:
#        
#       try:
#           distance_to_convert = float(input('Enter the distance, as a number: '))  
#           units_to_convert = input('What type of units are you converting: ')
#           units_to_convert = units_to_convert.lower()

#        except ValueError:
#           print("Invalid input, please enter a valid numerical distance.")
#           continue                     
                
#        if units_to_convert not in distances.keys():
#           print('"Invalid choice, valid unit types are: feet, miles, meters, kilometers, yards or inches.")')

#        else:
#           units_to_meters = distance_to_convert * distances.get(units_to_convert)
#           print(f'{distance_to_convert} {units_to_convert} is equal to {units_to_meters} meters.')
#           break
#
#main()





# Unit Converter - Version 3
#distances = {'feet': 0.3048, 'miles': 1609.34, 'meters': 1.0, 'kilometers': 1000, 'yards': 0.9144, 'inches': 0.0254}

#print('Welcome to the unit converter!')
#print(f'This program can convert: feet, miles, meters, kilometers, yards, inches.')

#def main():

#    while True:
#        
#       try:
#           distance_to_convert = float(input('Enter the distance, as a number: '))  
#           units_to_convert = input('What type of units are you converting: ')
#           units_to_convert = units_to_convert.lower()

#        except ValueError:
#           print("Invalid input, please enter a valid numerical distance.")
#           continue                     
                
#        if units_to_convert not in distances.keys():
#           print('"Invalid choice, valid unit types are: feet, miles, meters, kilometers, yards or inches.")')

#        else:
#           units_to_meters = distance_to_convert * distances.get(units_to_convert)
#           print(f'{distance_to_convert} {units_to_convert} is equal to {units_to_meters} meters.')
#           break
#
#main()






# Unit Converter -  Version 4
distances = {'feet': 0.3048, 'miles': 1609.34, 'meters': 1.0, 'kilometers': 1000, 'yards': 0.9144, 'inches': 0.0254}                      # dictionary containing units and their conversion rate

def unit_conversion(distance_to_convert, units_to_convert, meters_to_units):
    units_to_meters = distance_to_convert * distances.get(units_to_convert)                                                                                   # convert the meters into the desired second unit and print results
    converted_units = units_to_meters / distances.get(meters_to_units)
    return converted_units


print('Welcome to the unit converter!')
print(f'This program can convert: feet, miles, meters, kilometers, yards and inches.')

def main():

    continue_convert = 'Yes'

    while continue_convert == 'Yes':                                                                                                      # while loop to allow for repeated use
        user_input = input("Enter 'start' to begin, or 'exit' to quit: ")
        user_input = user_input.title()

        if user_input == 'Start':                                                                                                           
            
            while True:                                                                                                                   # loop to catch value errors if user does not enter a number or invalid choice for conversion

                try:
                    distance_to_convert = float(input('Enter the distance, as a number: '))         
                    units_to_convert = input('What type of units are you converting: ')
                    units_to_convert = units_to_convert.lower()
                    meters_to_units = input('What type of unit do you want to convert into: ')                                                
                    meters_to_units = meters_to_units.lower()

                except ValueError:
                    print("Invalid input, please enter a valid numerical distance.")
                    continue                     
                
                if units_to_convert not in distances.keys():
                    print('"Invalid choice, valid unit types are: feet, miles, meters, kilometers, yards or inches.")')

                elif meters_to_units not in distances.keys():
                    print("Invalid choice, valid unit types are: feet, miles, meters, kilometers, yards or inches.")

                else:
                    break

            converted_units = unit_conversion(distance_to_convert, units_to_convert, meters_to_units)
            print(f'{distance_to_convert} {units_to_convert} is {converted_units:.3f} {meters_to_units}.')

        elif user_input == 'Exit':                                                                                                        # exit program if user is finished
            print('Goodbye.')
            quit()

        else:                                                                                                                             # catch invalid inputs
           print('Invalid input. Please enter start or exit.')
           main()  

        continue_convert = input('Would you like to convert more values? Yes/No ')                                                        # ask user if they wish to repeat
        continue_convert = continue_convert.title()

    if continue_convert == 'No':                                                                                                          # exit if user is done
        print('Goodbye.')
        quit()

    else:                                                                                                                                 # catch invalid inputs
        print('Invalid input.')
        main()

main()
'''Version 1'''
#Ask user for distance in feet and convert it to meters. The ratio of ft to meters is 0.3048
print('Please provide the distance in feet and I will convert to meters \n')
user_input = float(input('This is Version 1. What is the distance?: '))
ft_to_m = 0.3048

print(f"You entered {user_input}ft which equates to {user_input * ft_to_m:.2f} meters.")

'''Version 2'''
#User will enter distance in either feet, miles, meters and kilometers which will be converted to meters

one_ft_to_m = 0.3048
one_mi_to_m = 1609.34
one_m_to_m  = 1
one_km_to_m = 1000

user_distance = float(input('\nThis is version 2. Please input the distance: '))
unit_of_distance = input("Please select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers:  ").lower()

if unit_of_distance == 'ft':
    converted_distance = user_distance * one_ft_to_m
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'mi':
    converted_distance = user_distance * one_mi_to_m
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'm':
    converted_distance = user_distance * one_m_to_m
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'km':
    converted_distance = user_distance * one_km_to_m
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance:.2f} meters")
else:
    print("I don't understand what you are trying to achieve. Goodbye")


'''Version Three'''
#This version requires adding yards and inches. 1 yard is 0.9144 and 1 inch equals 0.0254
#I can copy either copy the ratio below version two or I can create a dictionary which I can append version three.

unit_converter = {
    'one_ft_to_m': 0.3048,
    'one_mi_to_m': 1609.34,
    'one_m_to_m':  1,
    'one_km_to_m': 1000
}

unit_converter.update({
    'one_yd_to_m': 0.9144,
    'one_in_to_m': 0.0254
})

#print(unit_converter)
print('\nWelcome to version 3, we just added yard and inches to version 2.')
#Being a new version, I want to have the difference from above know to user also tell them that I have added yard and inch
user_distance = float(input('\nThis is version 3 . Please input the distance: '))
unit_of_distance = input("For version 3. Please select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers or 'yd' for yard or 'in' for inch:  ").lower()


if unit_of_distance == 'ft':
    converted_distance = user_distance * unit_converter['one_ft_to_m']
    print(f"You entered {user_distance}{unit_of_distance}, which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'mi':
    converted_distance = user_distance * unit_converter['one_mi_to_m']
    print(f"You entered {user_distance}{unit_of_distance}, which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'm':
    converted_distance = user_distance * unit_converter['one_m_to_m']
    print(f"You entered {user_distance}{unit_of_distance}, which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'km':
    converted_distance = user_distance * unit_converter['one_km_to_m']
    print(f"You entered {user_distance}{unit_of_distance}, which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'yd':
    converted_distance = user_distance * unit_converter['one_yd_to_m']
    print(f"You entered {user_distance}{unit_of_distance}, which is equal to {converted_distance:.2f} meters")
elif unit_of_distance == 'in':
    converted_distance = user_distance * unit_converter['one_in_to_m']
    print(f"You entered {user_distance}{unit_of_distance}, which is equal to {converted_distance:.2f} meters")

else:
    print("I don't understand what you are trying to achieve. Goodbye")


'''Version Four'''
#The goal of this version is to recieve an input in one unit and convert it to another ouput of a users choice. I can use meters as a median for conversion

print('\nFor version 4. Please provide an input distance and unit and I will convert it to your desired unit output! ')



one_feet_to_m = 0.3048
one_mile_to_m = 1609.34
one_meter_to_m  = 1
one_kilometer_to_m = 1000

input_distance = float(input('\nVersion 4. What is the input distance?: '))
input_unit = input("\nPlease select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers:  ").lower()

#Just as I did in Version 2, I will get the distance in meters before multiplying it with desired output. 
if input_unit == 'ft':
    converted_distance = one_feet_to_m * input_distance
    output_input = input("\nFor output. Please select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers:  ").lower()
    if output_input == 'mi':
        output_distance = converted_distance / one_mile_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} miles")
    elif output_input == 'm':
        output_distance = converted_distance / one_meter_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} meters")
    elif output_input == 'km':
        output_distance = converted_distance / one_kilometer_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} kilometers")
    elif output_input == 'ft':
        output_distance = converted_distance / one_feet_to_m
        print(f"\nNo changes since the input unit is same as output unit.")



elif input_unit == 'mi':
    converted_distance = one_mile_to_m * input_distance
    output_input = input("\nFor output. Please select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers:  ").lower()
    if output_input == 'mi':
        output_distance = converted_distance / one_mile_to_m
        print(f"\nNo changes since the input unit is same as output unit.")
    elif output_input == 'ft':
        output_distance = converted_distance / one_feet_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} feet")
    elif output_input == 'km':
        output_distance = converted_distance / one_kilometer_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} kilometers")
    elif output_input == 'm':
        output_distance = converted_distance / one_meter_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} meters")

elif input_unit == 'm':
    converted_distance = one_meter_to_m * input_distance
    output_input = input("\nFor output. Please select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers:  ").lower()
    if output_input == 'mi':
        output_distance = converted_distance / one_mile_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} miles")
    elif output_input == 'ft':
        output_distance = converted_distance / one_feet_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} feet")
    elif output_input == 'km':
        output_distance = converted_distance / one_kilometer_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} kilometers")
    elif output_input == 'm':
        output_distance = converted_distance / one_meter_to_m
        print(f"\nNo changes since the input unit is same as output unit.")



elif input_unit == 'km':
    converted_distance = one_kilometer_to_m * input_distance
    output_input = input("\nFor output. Please select either 'ft' for feet or 'mi' for miles or 'm' for meters or 'km' for kilometers:  ").lower()
    if output_input == 'mi':
        output_distance = converted_distance / one_mile_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} miles")
    elif output_input == 'ft':
        output_distance = converted_distance / one_feet_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} feet")
    elif output_input == 'km':
        output_distance = converted_distance / one_kilometer_to_m
        print(f"\nNo changes since the input unit is same as output unit.")   
    elif output_input == 'm':
        output_distance = converted_distance / one_meter_to_m
        print(f"\nYou entered {input_distance}{input_unit}, which equates to {output_distance:.4f} meters")

else:
    print('Please try again!')
      











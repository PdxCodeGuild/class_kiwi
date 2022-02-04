'''
#Ask the user for the number of feet, and print out the equivalent distance in meters. 

one_ft_to_m = 0.3048
user_input = float(input('Please enter the distance in feet: '))
print(f"You entered {user_input} feet, this equals {round(one_ft_to_m * user_input, 2)} meters.")

#Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
# ...The units we'll allow are feet, miles, meters, and kilometers.

one_ft_to_m = 0.3048
one_mi_to_m = 1609.34
one_m_to_m = 1
one_km_to_m = 1000


#print('Please enter a unit and I will convert it to meters!')
user = float(input('Please enter the distance: '))
dist_unit = input("What is the unit distance, please select either 'm' for meters or 'ft' for feet or 'mi' for miles or km for kilometer: ").lower()


if dist_unit == 'ft':
    dis_in_m = float(one_ft_to_m * user)
    print(f"You entered {user}{dist_unit}, this equals {dis_in_m} meters")


unit_convert = {
    'one_ft_to_m': 0.3048,
    'one_mi_to_m': 1609.34,
    'one_m_to_m': 1,
    'one_km_to_m': 1000

}

def convert_unit(unit_convert,user,dist_unit):

    if dist_unit == 'ft':
        dist_in_m = user * unit_convert['one_ft_to_m']
    
        return f"you enter {user}{dist_unit} which equates to {round(dist_in_m,2)} meters"

print(convert_unit(unit_convert,user,dist_unit))
#Add support for yards, and inches.

'''
"""
#Ask the user for the number of feet, and print out the equivalent distance in meters. 
print('Please enter distance in feet and I will convert it into meters!')
one_ft_to_meter = 0.3048
user_input = float(input('Please enter distance in feet: '))

print(f"You entered {user_input}ft which equates to {round(user_input * one_ft_to_meter, 2)} meters")
#Allow the user to also enter the units. Then depending on the units, convert the distance into meters. 
# ...The units we'll allow are feet, miles, meters, and kilometers.
"""
unit_convert = {
    'one_ft_to_m': 0.3048,
    'one_mi_to_m': 1609.34,
    'one_m_to_m':1,
    'one_km_to_m': 1000
}

#unit_convert.update({'one_yd_to_m': 0.9144, 'one_in_to_m': 0.0254})

print('Provide distance and unit of distance, i will convert to meters')
user_distance = float(input('Please enter the distance: '))
unit_of_distance = input("Please select unit of distance 'm' for meters or 'ft' for feet or 'km' for kilometer or 'mi' for miles: ").lower()
#unit_of_distance = input("Please select unit of distance 'm' for meters or 'ft' for feet or 'km' for kilometer or 'mi' for miles or 'yd' for yard or 'in' for inch: ").lower()

if unit_of_distance == 'ft':
    converted_distance = round(unit_convert['one_ft_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")
elif unit_of_distance == 'mi':
    converted_distance = round(unit_convert['one_mi_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")
elif unit_of_distance == 'm':
    converted_distance = round(unit_convert['one_m_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")
elif unit_of_distance == 'km':
    converted_distance = round(unit_convert['one_km_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")


"""
elif unit_of_distance == 'yd':
    converted_distance = round(unit_convert['one_yd_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")
elif unit_of_distance == 'in':
    converted_distance = round(unit_convert['one_in_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")
"""

#Add support for yards, and inches.
#Appending the dictionary to include yard and inch. Then will have to append on the unit_of_distance and above condition


'''
unit_convert.update({'one_yd_to_ft': 0.9144, 'one_in_to_m': 0.0254})
unit_of_distance = input("Please select unit of distance 'm' for meters or 'ft' for feet or 'km' for kilometer or 'mi' for miles or 'yd' for yard or 'in' for inch: ").lower()


if unit_of_distance == 'yd':
    converted_distance = round(unit_convert['one_yd_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")
elif unit_of_distance == 'in':
    converted_distance = round(unit_convert['one_in_to_m'] * user_distance, 2)
    print(f"You entered {user_distance}{unit_of_distance} which is equal to {converted_distance} meters")

However above formula has to be merged with second options to make sense

'''

"""
unit_convert = {
    'one_ft_to_m': 0.3048,
    'one_mi_to_m': 1609.34,
    'one_m_to_m':1,
    'one_km_to_m': 1000,
    'one_yd_to_m': 0.9144, 
    'one_in_to_m': 0.0254
}
#I will get a distance, will then convert it to meters and return the distance in requested output unit
dist_ance = float(input('What is the distance: '))
input_units = input('What are the input units: ').lower()
#output_units = input('What are the output unit: ').lower()

def multiple_conver(dist_ance, input_units): #output_units)

    if input_units == 'ft':
        new_dis_in_m = dist_ance * unit_convert['one_ft_to_m']
        output_units = input('What are the output unit: ').lower()
        if output_units == 'mi':
            output_dist = new_dis_in_m / unit_convert['one_mi_to_m']
            return f"{dist_ance}{input_units} equates to {output_dist:.4f} miles"


print(multiple_conver(dist_ance, input_units)) #output_units))

"""
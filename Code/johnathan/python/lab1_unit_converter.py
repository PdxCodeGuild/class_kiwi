# This lab will involve writing a program that allows the user to convert a number between units.
# Each version should be accomplished using a dictionary and each can be completed without the use of if/elif statements.

#################################################################### Version 1 ######################################################################################

# metrics_dict = {'1ft': 0.3048}
# number_ft = input("What is the number of feet?: ")
# print(number_ft)

# number_ft = int(number_ft)
# output = metrics_dict['1ft'] * number_ft

# print(f'ft, is {output} in meters')


#################################################################### Version 2 #######################################################################################
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
# Hint: Try using the unit as the key and the conversion as the value.
################################################################### Version 3 ############################################################################################
# Add support for yards, and inches.

#Metrics dictionary 
metrics_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000}

new_items = {
    'yard': 0.9144,
    'inch': 0.0254}
metrics_dict.update(new_items)

print(metrics_dict)
#Ask the user the distance or length of measurement to be converted.
object_length = input('Enter the distance of measurement: ')
#Ask the user to input the unit to be converted to meters. 
units_measure = input(f'What are the units of measurement? Choose from {metrics_dict}: ')
#Associate user selection with the dictionary to prompt dictionary/conversion. 
units_conv = metrics_dict [units_measure]
#Convert the object_length to an integer. 
object_length = int(object_length)
#Calculate inputted 'object_length' with the 'units_conv'
final_conv = object_length * units_conv
#create a new variable to convert units inputted by the user, to user selected output units. 
v4user_output_selection = input(f'Select the desired units, you would like the distance to be converted into. Your options are, n\"{metrics_dict}": ')
v4units_conv = metrics_dict[v4user_output_selection]
version4_output = final_conv / v4units_conv
#print(f'{object_length} {units_measure} is {final_conv} in meters.')
# V4 print statement 
print(f'{object_length} {units_measure} is {version4_output} {v4user_output_selection}.')

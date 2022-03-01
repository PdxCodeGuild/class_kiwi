

'''

VERSION 1

# Meters is the amount of meters per foot
meters = .3048
# Asks user to input a distance in feet and turns input into a float
user_distance = float(input("Enter a distance in feet: "))
# Takes the user input and multiplies it by the meters. Also rounds the dec points
final_distance = round(meters * user_distance, 4)

print( f"{user_distance}ft is {final_distance} meters")

'''


'''

VERSION 2

# Base numbers for each unit
m_meter = 1
mi_meter = 1609.34
ft_meter = .3048
km_meter = 1000

# Collects user inputs such as what unit they'd like to convert and the distance
user_unit = input("Chose a unit to convert (ft, mi, m, or km): ")
user_distance = float(input( f"Enter how many {user_unit}(s) you'd like to convert: "))

# defines which unit the user input and outputs the correct conversion
if user_unit == 'm':
    print( f"{user_distance}{user_unit} is {round(m_meter * user_distance, 4)} meters")
elif user_unit == 'mi':
    print( f"{user_distance}{user_unit} is {round(mi_meter * user_distance, 4)} meters")
elif user_unit == 'ft':
    print( f"{user_distance}{user_unit} is {round(ft_meter * user_distance, 4)} meters")
elif user_unit == 'km':
    print( f"{user_distance}{user_unit} is {round(km_meter * user_distance, 4)} meters")
# If the inputted unit isn't one of the options the user will know 
else:
    print(f"{user_unit} is not one of the options.")

'''




'''

VERSION 3


# Base numbers for each unit
m_meter = 1
mi_meter = 1609.34
ft_meter = .3048
km_meter = 1000
yd_meter = .9144
in_meter = .0254

# Collects user inputs such as what unit they'd like to convert and the distance
user_unit = input("Chose a unit to convert (ft, mi, m, km, yd, or in): ")
user_distance = float(input( f"Enter how many {user_unit}(s) you'd like to convert: "))

# defines which unit the user input and outputs the correct conversion
if user_unit == 'm':
    print( f"{user_distance}{user_unit} is {round(m_meter * user_distance, 4)} meters")
elif user_unit == 'mi':
    print( f"{user_distance}{user_unit} is {round(mi_meter * user_distance, 4)} meters")
elif user_unit == 'ft':
    print( f"{user_distance}{user_unit} is {round(ft_meter * user_distance, 4)} meters")
elif user_unit == 'km':
    print( f"{user_distance}{user_unit} is {round(km_meter * user_distance, 4)} meters")
elif user_unit == 'yd':
    print( f"{user_distance}{user_unit} is {round(yd_meter * user_distance, 4)} meters")
elif user_unit == 'in':
    print( f"{user_distance}{user_unit} is {round(in_meter * user_distance, 4)} meters")
# If the inputted unit isn't one of the options the user will know 
else:
    print(f"{user_unit} is not one of the options.")

'''


'''

VERSION 4 - OPTIONAL
#** There is probably a more simple way to acheive the same result however this is the way that i could find to work!




# Base meter values

m_meter = 1
mi_meter = 1609.34
ft_meter = .3048
km_meter = 1000
yd_meter = .9144
in_meter = .0254

# User inputs 
user_distance = float(input("Enter a distance: "))
user_input_unit = input("Enter the input unit: ")
user_output_unit = input("Enter the output unit: ")

# Converts user units into meters(floats)
if user_input_unit == 'm':
    user_meter_unit = m_meter
elif user_input_unit == 'mi':
    user_meter_unit = mi_meter
elif user_input_unit == 'ft':
    user_meter_unit = ft_meter
elif user_input_unit == 'km':
    user_meter_unit = km_meter
elif user_input_unit == 'yd':
    user_meter_unit = yd_meter
elif user_input_unit == 'in':
    user_meter_unit = in_meter

# Converts user units into meters(floats)
if user_output_unit == 'm':
    user_meter_out_unit = m_meter
elif user_output_unit == 'mi':
    user_meter_out_unit = mi_meter
elif user_output_unit == 'ft':
    user_meter_out_unit = ft_meter
elif user_output_unit == 'km':
    user_meter_out_unit = km_meter
elif user_output_unit == 'yd':
    user_meter_out_unit = yd_meter
elif user_output_unit == 'in':
    user_meter_out_unit = in_meter


distance_meters_input = user_distance * user_meter_unit

final_conversion= round(distance_meters_input / user_meter_out_unit, 4)

print( f"{user_distance} {user_input_unit} is {final_conversion} {user_output_unit}")

'''
##Unit Converter

#version1
#ask for input in feet and output in meters
# 1ft is 0.3048m

# distance=input("what is the distance in feet? ")
# meter_conversion=int(distance)*.3048
# meter_conversion=round(meter_conversion, 4)
# print(f"{distance} ft is {meter_conversion}m")

#version 2 
#additional distances
# create a conversion repository
# conversion = {
#     'ft' : .3048,
#     'mi' : 1609.34,
#     'm' : 1,
#     'km' : 1000
# }

# #setup the input variables
# distance=input("what is the distance? ")
# distance=int(distance)

# unit=input("what are the units? choose ft, mi, km: ")

# #pull from dictionary
# if unit in conversion:
#     converted_distance = conversion[unit]
#     distance_in_meters = converted_distance * distance
#     print(f"{distance} {unit} is {round(distance_in_meters,2)} m")

# else:
#     print("unit not recognized")



# #version 3

# conversion = {
#     'ft' : .3048,
#     'mi' : 1609.34,
#     'm' : 1,
#     'km' : 1000,
#     'yd' : .9144,
#     'in' : .0254
# }

# #setup the input variables
# distance=input("what is the distance? ")
# distance=int(distance)

# unit=input("what are the units? choose ft, mi, km, in, yd: ")

# #pull from dictionary
# if unit in conversion:
#     converted_distance = conversion[unit]
#     distance_in_meters = converted_distance * distance
#     print(f"{distance} {unit} is {round(distance_in_meters,2)} m")

# else:
#     print("unit not recognized")

#version 4

#input values
conversion_in = {
    'ft' : .3048,
    'mi' : 1609.34,
    'm' : 1,
    'km' : 1000
}

conversion_out = {
    'ft' : 1/.3048,
    'mi' : 1/1609.34,
    'm' : 1,
    'km' : 1/1000
}

#build input
distance=input("what is the distance? ")
distance=int(distance)

unit_in=input("what are the input units? choose ft, mi, km: ")
unit_out=input("what are the output units? choose ft, mi, km: ")

#enter sausage maker
if unit_in in conversion_in and unit_out in conversion_out:
    converted_to_meters = conversion_in[unit_in]
    distance_in_meters = converted_to_meters * distance
    meters_out = conversion_out[unit_out]
    final_conversion = meters_out * distance_in_meters
    print(f"{distance}{unit_in} is {round(final_conversion,4)}{unit_out}")

else:
    print("unit not recognized")
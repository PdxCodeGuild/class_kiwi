# ask for distance
distance = int(input("What is the distance? "))
# ask for unit
input_units = input("What are the input units (ft, mi, m, km,)?: ")
# output unit
output_units = input("What are the output units (ft, mi, m, km,)?: ")

# convert from unit to meters
feet_meter = distance * 0.3048
miles_meter = distance * 1609.34
meter_meter = distance
kilo_meter = distance * 1000

###  Lab 1 Practice  ###
################################
##                            ##
## Lab 1: Unit Converter      ##
##   Author: Anthony Bilie    ##
##   Date: 2/13/2022          ##
##                            ##
################################


# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.
# > what is the distance in feet? 12
# > 12 ft is 3.6576 m

# Ask User for number of feet
distance = input("What is the distance in feet? ")
# convert string to int
distance = int(distance)
# conversion from feet to meters
meters = 0.3048
meters_converstion = distance * meters
# print out feet in meters(output)
print(f"{distance} ft is {round(meters_converstion,4)} m. ")

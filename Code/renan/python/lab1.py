#Version 1
#What is the distance in feet? 12
#12 ft is 3.6576 m
#I first will create a dictionary to define my units for all versions of lab
distance = {
    'ft': 0.3048,
    'yrd':0.9144,
    'in': 0.0254,
    'mi': 1609.34,
    'km': 1000.00,
    'm' : 1 
        
}

#Ask the user for the distance in feet, and print out in meters

number = input("Regarding meters what is the distance in feet?: ")

total = int(number) * distance['ft']

print(total)

#Version 2
#What is the distance? 100
#What are the units? mi
#100mi is 160934 m

number = input("What is the distance?: ")

units = input("What are the units, 'ft', 'yrd', 'in', 'mi', 'km', 'm'?: ")

total = int(number) * distance['mi']

print(total) 

#Version 3 Add Support for Yards and Inches

number = input("How many yards?: ")

total = int(number) * distance['yrd']

print(total)

number = input("How many inches?: ")

total = int(number) * distance['in']

print(total)

#Version 4 (Will have to create a new Dictionary)
length = {
    'ft': 5280,
    'mi': 1  
           
}

#What is the distance? 100
#What are the input units? ft
#What are the output units? mi
#100 ft is 0.0189394 mi

number = input("What is the distance?: ")

total = int(number) / length['ft']

print(total) 
                       
#  Ask user to enter a distance in feet input
#  Version 1
user_distance = input("What is the distance in feet?")
print(f"{user_distance} is equal to 3.6576 m ")



user_distance = input("What is the distance?")
user_units = input("What are the units 'ft','mi','m','km'? ")

# Version 2
#  Create a dictionary to hold a key and value for distance to Meter conversion.
my_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}
#  this is the answer to the user's inputs
solution = (my_dict[user_units] * int(user_distance))
print(f'{user_distance} {user_units} is {solution} m. ')

# Version 3 
#  I will add to my_dict to be able to convert with yards and inches

user_distance = input("What is the distance?")
user_units = input("What are the units 'ft','mi','m','km','yd',in? ")



my_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
}

my_dict["yd"] = 0.9144
my_dict["in"] = 0.0254
solution = (my_dict[user_units] * int(user_distance))
print(f'{user_distance} {user_units} is {solution} m. ')
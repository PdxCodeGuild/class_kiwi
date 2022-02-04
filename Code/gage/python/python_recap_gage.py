
'''

print("Hello World!")               # String
print(18)                           # Integer
print(18.5)                         # Float
print(False)                        # Boolean
print([2, 4, 6 ,8])                 # List
print({'a': 11, 'b': 22, 'c': 33})  # Dictionary



greeting = "Hello World!"           # Var
name = input("Enter name: ")        # Input


user_color = input("What is your favorite color?: ")
print(f"I like {user_color} aswell!")

age = int(input("Enter your age: "))
print( f"You're {age} years old?!")


price = float(input("Enter the price of the item: "))


#print( f"you have a 50% off coupon! Your total is ${discount_price}")


# when the price is between 50 and 75 it will give a 10% discount
if price >= 50.0 and price <= 75:
    price = round(price * .9, 2)
    print( f"you have a 10% off coupon! Your total is ${price}")
# when the price is between 75 and 100 it will give a 50% discount
elif price >= 75 and price <= 100:
    price = round(price * .5, 2)
    print( f"You have a 50% off coupon! Your total is ${price} ")
# when the price is above 100 it will give a 75% discount
elif price > 100:
    price = round(price * .25, 2)
    print( f"You have a 75% off coupon! Your total is ${price}")
# when the price is below 50 it won't give a discount
else:
    print( f"Your total is ${price}")




price = float(input("Enter the price of the item: "))
membership = input("Are you a member? y/n: ").lower()

if membership == 'y':
    price = round(price * .5, 2)
    print( f"Welcome back member. heres a 50% discount! your total is ${price} ")
elif membership == 'n': 
    print( f"Ok your total is ${price}")
else: 
    print( f"Invalid response: Expected 'y' or 'n' and you entered '{membership}'")

'''

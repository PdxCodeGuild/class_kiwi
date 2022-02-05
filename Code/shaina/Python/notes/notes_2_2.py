"Hello World!"

# print("Hello World!")

# print(4)

# print(2.3)

# print(True)

# print([1, 2, 3, 4])

# print(type("Hi there, this is a type string"))

# input("Enter your name:")

# print("Hello Brian")

# print("Hello", input("Enter your name: "))

# greeting = "Hello World!"

# print(greeting)

# greeting = "Hello"
# name = input("Enter your name: ")

# print(greeting, name)

# color = input("What is your favorite color? ")
# print(f"I like {color} too!")

# number = 13
# print(f"I have {number} cats.")

# age = int(input("enter your age: "))
# age = input("enter your age: ") # Always returns a string
# age = int(age)
# print(f'Wow you are old, cant believe you are {age + 50}')


"""
price = float(input("Enter the price of your item: "))
# price is between $50 and $75, give a 10% discount
if price > 50 and price <= 75:
    price = round(price * .9, 2)
    print(f"Your total today is ${price}. This includes a 10% discount.")
# price is between 75 and 100, give a 15% discount
elif price > 75 and price <= 100:
    price = round(price * .85, 2)
    print(f"Your total today is ${price}. This includes a 15% discount.")
# price is over $100, give a 20% discount
elif price > 100:
    price = round(price * .8, 2)
    print(f"Your total today is ${price}. This includes a 20% discount.")
else:
    print(f"Your total today is ${price}")
"""

# Ask the user for the price of their item
price = float(input("Enter the price of your item: "))

# Ask the user if they are a member
user = input("Are you a member? ").lower()

# if user is a member, apply 20% discount
if user == "yes":
    price = price * .8
    print(f"Your total is ${price:.2f}. Enjoy your 20% discount for being a member.")

# otherwise, show them full price
else:
    print(f"Your total is ${price:.2f}. You could have saved ${price * .2:.2f} by having a membership.")
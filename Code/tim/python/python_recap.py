"""
# A = "Hello world!"
# print("Hello World!")
# print(A)
# print(4)
# print(2.3)
# print(True)
# print([1, 2, 3, 4])
# print(type("Hi there, this is a type string"))

# print("Hello", input("Enter your name: "))

# greeting = "Hellow World!"

# print(greeting)

# name = input("Enter your name: ")
# greeting = "Hello"


# print(greeting, name)

# color = input("Please enter your favorite color: ")

# print(f"I like {color} too!")

# number = 47
# print(f"I have {number} cats.")

# age = input("Enter your age: ")
# age = int(age)


# print(f"Wow you are old, cant believe you are {age + 50}")

price = float(input("Enter the price of your item: "))
# if price is between $50 and 75$ give a 10% discount
if price > 50 and price <= 75:  

    price = round(price * .9, 2)
    print(f"Your total today is ${price}. This includes a 10% discount.")
# if price is between $75 and $100 give a 15% discount
elif price > 75 and price <= 100:
    price =round(price * .85, 2)
    print(f"Your total today is ${price}. This includes a 15% discount.")
#if the price is over $100 give a 20% discount

elif price > 100 :
    price = round(price * 0.8, 2)
    print(f"Your total today is ${price}. This includes a 20% discount.")

else:
    print(f"Your total today is ${price}")
"""


# Ask the user for the price of their item

# Ask the user if they are a member

# if user is a member, apply 20% discount
price = float(input("Enter the price of your item: "))
# Otherwise, Show them the full price
user = input("Are you a member? ").lower()


if user == "yes":
    price = price * .8
    print(f"Your total price is ${price:.2f}. Enjoy your 20% discount for being a member!")
    
elif user == "no":
    print(f"Your total price is ${price:.2f}. You could have saved ${round(price * .2, 2)}")
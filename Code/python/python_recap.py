
#print Hello World
# print("Hello World!")



# print(4)

# print(2.3)

# print(True)


# print([1,3,5,7])

# print(type("hello"))

# input("Enter your name: ")

# print("Hello Joey")

# print("Hello", input("Enter your name: "))

# greeting = "Hello World!"

# print(greeting)

# greeting = "Hello"
# name = input("Enter a name: ")

# print(greeting, name)

# color = input("What's your favorite color? ")

# message = print(f"Hey I like {color} too!")

# number = 47

# print(f"I have {number} cats.")


# age = int(input("enter your age: "))
# print(f" Wow you are old, cant believe you are {age + 50}.")

"""
price = float(input("Enter the price of your item: "))
if price > 10 and price <= 25:
    price = round(price * .9, 2)
    print(f"you received a discount, your total today is {price}!")
elif price > 25:
        price = round(price * .75, 2)
        print(f"you received a discount, your total today is {price}!")
else: print(f"Your total today is {price}.")

"""


# Ask the user for the price of their item
price = float(input("Enter the price of your item: "))
# Ask the user if they are member
user = input("are you a member? ").lower()
#  If user is a member, apply 20% discount
if user == "yes":
# otherwise, show them full price
    price = round(price * .8, 2)
    print(f"after your discount your total is ${price}")
else: 
    print(f"your total today is ${price}")
#print("hello",input("input your name") )



#greeting = "hello world!!!!"
#print(greeting)
# greeting = "hello"
# name = input("enter your name  ")
# print(greeting, name)

# color = input("what is your favorite color? ")
# print(f"I like {color} too!")

# number = 47
# print(f"I have {number} cats. ")

# age = input("enter your age: ")
# age = int(age)
# print(f"wow you old, cant believe you are {age + 50}")

"""
price = float(input("enter price of item  "))
if price > 50 and price <= 75:
    price = round(price * .9)
    print(f" your total is $ {price}. this includes 10% discount. ")
#price is between 75 and 100 , give 15% discount    
elif price > 75 and price <= 100:
    price = round(price * .85)     
    print(f" your total is $ {price}. this includes 15% discount. ")
elif price > 100:
    price = round(price * .8)     
    print(f" your total is $ {price}. this includes 20% discount. ")
else: 
    print(f" your total is {price}")
"""
# ask usr for price and if thy are member
price = float(input("price:  "))
user = input("member? ").lower
if user == "yes":
    price = price * .8
    print(f"your total is {price}. enjoy your 20% discount. ")

elif user == "no":
    price = price
    print(f"your total is {price}. you could have saved {price * .2} by having a membership")


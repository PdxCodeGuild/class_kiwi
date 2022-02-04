'''
price = float(input("Enter the price of your item: "))
if price >= 50 and price < 75:
    price = round(price * .5, 2)
    print(f"Your total today is ${price}. This includes a 50% discount.")
elif price >= 75 and price < 100:
    price = round(price * .85, 2)
    print(f"Your total today is ${price}. This includes a 15% discount.")
elif price >= 100:
    price = round(price * .80, 2)
    print(f"Your total today is ${price}. This includes a 20% discount.")
else:
    print(f"Your total today is ${price}")
'''
# Ask the user for the price of their item
price = float(input("Enter the price of your item: "))
# Ask the user if they are a member
member = input("Are you a member? ").lower()
# If the user is a member, apply 20% discount
if member == "yes":
    price = price * .8
    print(f"Your total is ${price:.2f}. This includes a membership discount of 20%.")
# Otherwise, show them full price
else:
    print(f"Your total is ${price:.2f}. You could have saved ${price * .2:.2f} by having a membership.")

# print('Hello')

# number = int(input('Enter a number: '))

# print(f'{number + 50} "your number plus 50" ')

# ---

# price = float(input('What is the price? :')) # 19.99

# price = round(price * .5, 2) 

# print(price) # 9.99

#-- -

# price = float(input('What is the price? :')) # 19.99

# if price >= 50:
#     price = round(price * .5, 2)
#     print(f'Your price is ${price} this includes a 50% discount') # 9.99
# else:
#     print(f'Your price is ${price}')

# ---

# if price > 50 and price < 74:
#     price = round(price * .9, 2)
#     print(f'Your price is ${price} this includes a 10% discount') 
# elif price >= 75 and price < 100:
#     price = round(price * .85, 2)
#     print(f'Your price is ${price} this includes a 15% discount') 
# elif price  >= 100:
#     price = round(price * .8, 2)
#     print(f'Your price is ${price} this includes a 20% discount')

# price = float(input('What is the price? :'))
# membership = input('Do you have a Membership?: ') .title()


# if price > 50 and price < 74:
#     price = round(price * .9, 2)
#     print(f'Your price is ${price} this includes a 10% discount') 
# elif price >= 75 and price < 100:
#     price = round(price * .85, 2)
#     print(f'Your price is ${price} this includes a 15% discount') 
# elif price  >= 100:
#     price = round(price * .8, 2)
#     print(f'Your price is ${price} this includes a 20% discount')


# if membership == 'Yes':
#     price = round(price * .8, 2)
#     print(f'Your price is ${price:2f} this includes a 20% discount')  # price:2f prints .00 two decimal places
# else:
#     print(price)


# else:
#     print(f'Your price is ${price}')

# --

user = input('Enter your name: ')
if user:
    print(f'Hello {user}')
 


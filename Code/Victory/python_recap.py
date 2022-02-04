'''
'Hello world'

#print('Hello world')
greeting = input('Your name')


color = int(input('age: '))
print("I like " + color + " too")

age = int(input('num: '))
print(f"Wow you are old {age + 50}")


price = input('Please enter a price of item: ')
price = float(price)
while True:
    if price >= 50:

        new_price = price * 0.5
        print(round(new_price))
    else:
        print("Price less for discount")



#create a code that checks for membership, if member give 20% else show full price
price = float(input('Enter the price of your item: '))
user = input('Are you a member?: ').lower()

if user == 'yes':
    price = price * 0.8
    print(f"As a member, your price is {price:.2f}")
else:
    print(f"your price is {price:1f}. As a member you could have save {price * 0.2}")
'''



full_names = [
    "bruce banner"
    "peter parker"
    "tony stark"
]

first_names = full_names.copy()

for i in range(len(first_names)):
    first_names[i] = first_names[i].split(' ')[0][2]

print(first_names)
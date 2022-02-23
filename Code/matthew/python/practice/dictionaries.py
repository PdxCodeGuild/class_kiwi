

from random import choice


pet = {
    'name': 'Rocky',
    'breed': 'rock',
    'size': 'large',
    'nickname': 'roxie'
}

pet_dog = {
    'name': 'dog',
    'breed': 'dog',
    'size': 'large',
    'nickname': 'cat',
    'age': 3
}

# print(pet) # {'name': 'Rocky', 'breed': 'rock', 'size': 'large', 'nickname': 'roxie'}

# print(pet['name'])  # Rocky

# if 'age' in pet_dog:
#     print(pet_dog['age'])
# else:
#     print('No age found')


# .get() method is a safer way to access dictrionary values

# # age = pet_dog.get('age')
# print(age)  # 3 or None if no 'age' found

age = pet.get('age', 0)
# print(age)  # 3 or 0 if no 'age' found

# update the value of a dictionary item
pet_dog['age'] = 4

# print(pet_dog['age']) # 4

# new key: value pair
pet_dog['weight'] = 95
# print(pet_dog) #{'name': 'dog', 'breed': 'dog', 'size': 'large', 'nickname': 'cat', 'age': 4, 'weight': 95}

# delete key:value pair
del pet_dog['nickname']


# updat with new info
pet = {
    'name': 'Rocky',
    'breed': 'rock',
    'size': 'large',
    'nickname': 'roxie'
}

pet.update({'name': 'new rock', 'size': 'Small',
           'nickname': None, 'shade': 'greyish'})

# {'name': 'new rock', 'breed': 'rock', 'size': 'Small', 'nickname': None, 'shade': 'greyish'}
# print(pet)

# method to get all keys from dictonary
attributes = pet.keys()
# print(attributes)  # dict_keys(['name', 'breed', 'size', 'nickname', 'shade'])

# method to get all values from dictonary
values = pet.values()
# print(values)  # dict_values(['new rock', 'rock', 'Small', None, 'greyish'])

# method to get all key:value pairs from a dictronary
pairs = pet.items()
# dict_items([('name', 'new rock'), ('breed', 'rock'), ('size', 'Small'), ('nickname', None), ('shade', 'greyish')])
# print(pairs)

# loops over keys
for key in pet:
    break
    print(key)

# prints key:value pairs
for key, value in pet.items():
    break
    print(key, value)
"""
build contact list

contacts = [
    {'name': '', 'phone number': '','fav color':''},
    {'name': '', 'phone number': '','fav color':''},
    {'name': '', 'phone number': '','fav color':''},
]

"""
contacts = [{'name': 'jerry', 'phone number': '123456', 'fav color': 'blue'},
            {'name': 'jessica', 'phone number': '546454', 'fav color': 'green'}]

while True:
    choic = input('Choose: add, search, update, delete or exit ')
    if choic == 'exit':
        break
    elif choic == 'add':
        name = input('enter the contacts name')
        phone_num = input(f'Enter {name}s phone number')
        fav_color = input(f'Enter {name}s favorite color')
        contacts.append(
            {'name': name, 'phone number': phone_num, 'fav color': fav_color})
    elif choic == 'search':
        search = input('enter the name of the contact ')
        for contact in contacts:
            if contact['name'] == search:
                print(contact['name'])
                print(contact['phone number'])
                print(contact['fav color'])

    elif choic == 'update':
        search_name = input('Enter the name of the contact: ')
        for contact in contacts:
            if contact['name'] == search_name:

                correct = input(f"Is {contact['name']} correct? y/n ")

                if correct == 'n':
                    name = input('enter name')
                    contact['name'] = name

                correct = input(f"Is {contact['phone num']} correct? y/n ")

                if correct == 'n':
                    phone_number = input('Enter a phone number')
                    contact['phone num'] = phone_number

                correct = input(f"Is {contact['fav color']} correct? y/n ")
                if correct == 'n':
                    contact['fav color'] = input('Enter their favorite color')

    elif choic == 'delete':
        for i, contact in enumerate(contacts):
            print(f"{i}, , {contact['name']}")
        delete = int(input('Enter the number of the person you would like to delete'))
        contacts.pop(delete)
    else:
        break
print(contacts)
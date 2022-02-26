import json

contacts = []
with open('contacts.json',) as file:
    contents = file.read()
contacts = json.loads(contents)    

while True:
    choic = input('Choose: add, search, update, delete or exit ')
    if choic == 'exit':
        break
    elif choic == 'add':
        name = input('enter the contacts name: ')
        phone_num = input(f'Enter {name}s phone number: ')
        fav_color = input(f'Enter {name}s favorite color: ')
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
                    name = input('enter name: ')
                    contact['name'] = name
                correct = input(f"Is {contact['name']} correct? y/n ")

                correct = input(f"Is {contact['phone number']} correct? y/n ")
                if correct == 'n':
                    phone_number = input('Enter a phone number: ')
                    contact['phone num'] = phone_number

                correct = input(f"Is {contact['fav color']} correct? y/n ")
                if correct == 'n':
                    contact['fav color'] = input('Enter their favorite color: ')

    elif choic == 'delete':
        for i, contact in enumerate(contacts):
            print(f"{i}, , {contact['name']}")
        delete = int(input('Enter the number of the person you would like to delete: '))
        contacts.pop(delete)
    else:
        with open('contacts.json', 'w') as file:
            file.write(json.dumps(contacts))
        break



# print(contacts)
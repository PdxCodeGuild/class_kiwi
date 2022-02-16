

pet = {"name": "Rocky", "breed": "rock",
       "size": "large", "nickname": "roxie", 1: "Can be an integer"}

pet_dog = {"name": "Cloud", "breed": "boxer",
           "size": "large", "nickname": "Cloudy butt", 1: "why not", "age": 3}

# if "age" in pet:
#     print(pet["age"])
# else:
#     print("No age found.")


# .get() method is a safer way to access dictionary values
age = pet_dog.get("age", False)

# update a value
pet_dog["age"] = 4

# new key: value pair
pet_dog["weight"] = 95

# delete key:value pair
del pet_dog[1]
# pet_dog[1] = None


pet = {"name": "Rocky", "breed": "rock",
       "size": "large", "nickname": "roxie", 1: "Can be an integer"}

# Update old info or add new info
pet.update({"name": "Pearl", "size": "medium",
           "nickname": None, "shade": "gray"})


# method to get all keys from dictionary
attributes = pet.keys()
# print(attributes)

# method to get all values from dictionary
values = pet.values()
# print(values)

# method to get all key:value pairs from a dictionary
pairs = pet.items()
# print(pairs)

# for key in pet:  # looping over a dictionary will only give key
#     print(key)


# for key, value in pet.items():  # will give key and value when looping
#     print(key, value)


# contacts = [
#     { "name": "", "phone_number": "", "fav_color": ""},
#     { "name": "", "phone_number": "", "fav_color": ""},
#     { "name": "", "phone_number": "", "fav_color": ""},
# ]


# Let's create a small phonebook using dictionaries

# Start with 3 contacts for easy testing
contacts = [
    {'name': 'Susan', 'phone_number': '12312312', 'fav_color': 'Blue'},
    {'name': 'Bob', 'phone_number': '9832743892', 'fav_color': 'Red'},
    {'name': 'George', 'phone_number': '983472432', 'fav_color': 'Green'}
]

while True:
    # Show a menu of choices for the user
    choice = input("Choose: add, search, update, delete, exit: ")

    # If user chooses 'add', prompt them for a new contact name, phone number and favorite color
    if choice == 'add':
        name = input("Enter the contacts name: ")
        phone_number = input(f"Enter {name}'s phone number: ")
        fav_color = input(f"Enter {name}'s favorite color: ")

        # Add new information to the contacts
        contacts.append(
            {"name": name, "phone_number": phone_number, "fav_color": fav_color})

    # If user chooses 'search' ask them for the name of a contact and show their information
    elif choice == 'search':
        search_name = input("Enter the name of the contact: ").lower()
        # Loop over all contacts
        for contact in contacts:
            # If name entered matches a name in the contacts print the information
            if contact['name'].lower() == search_name:
                print(contact['name'])
                print(contact['phone_number'])
                print(contact['fav_color'])

    # If user chooses 'update', ask for name of contact
    elif choice == 'update':
        search_name = input("Enter the name of the contact: ").lower()
        # Loop over all contacts
        for contact in contacts:
            # If name entered matches a name in the contacts ask the user if the information is correct
            if contact['name'].lower() == search_name:
                # Check to see if name is correct
                correct = input(f"Is {contact['name']} correct? y/n: ")
                # If name is incorrect ask them for new data
                if correct == 'n':
                    name = input("Enter new name for contact: ")
                    contact['name'] = name
                # Check if phone number is correct
                correct = input(f"Is {contact['phone_number']} correct? y/n: ")
                # If phone number is incorrect ask them for new data
                if correct == 'n':
                    phone_number = input(
                        "Enter new phone number for contact: ")
                    contact['phone_number'] = phone_number
                # Check if favorite color is correct
                correct = input(f"Is {contact['fav_color']} correct? y/n: ")
                # If favorite color is incorrect ask for updated data
                if correct == 'n':
                    contact['fav_color'] = input(
                        "Enter new favorite color for contact: ")

                # Show updated contact information
                print(contact['name'])
                print(contact['phone_number'])
                print(contact['fav_color'])

    # If user chooses 'delete' ask them number of contact to delete (this happens to be the index of the contact in our list)
    elif choice == 'delete':
        for i, contact in enumerate(contacts):
            print(f"{i}. {contact['name']}")

        index = input("Enter the number of the contact you wish to delete: ")
        removed_contact = contacts.pop(int(index))
    else:
        break

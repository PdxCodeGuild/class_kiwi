fruits = ["apple", "banana", "citrus"]

fruits.append("dragon fruit")

# fruits.append(4)

# fruits.append(True)

# fruits.append(['red', 'green', 'blue'])

# fruits[-1] = "cantelope"

# remove item with index
# fruits.pop(2)

# remove item with element
# fruits.remove("banana")

# fruits.sort(reverse=True)

# new_fruits = fruits.copy()

# fruits.append('blueberry')

# print(fruits)
# print(new_fruits)


# Why use copy?
full_names = [
    "bruce banner",
    "peter parker",
    "tony stark"
]

# first_names = full_names.copy()

# for i in range(len(first_names)):
#     first_names[i] = first_names[i].split(' ')[0]

# print(full_names)
# print(first_names)


# print(full_names[0])
# print(full_names[1])
# print(full_names[2])
# print(full_names[3])
# print(full_names[4])
# print(full_names[5])
# print(full_names[6])


# for name in full_names:
#     print(name)


# num = 0
# while num < 12:
#     num = num + 1
#     print(num, 'Hello World!')


# greeting = "Hello Class Kiwi"

# for char in greeting:
#     print(char)


# colors = ['red', 'green', 'blue', 'yellow']

# for color in colors:
#     print(color)


# person = {
#     'first_name': 'Joe',
#     'last_name': 'Shmoe',
#     'age': 37,
#     'fav_color': 'green'
# }

# for key in person:
#     print(key)


while True:
    print('Hello')
    name = input('Enter your name')
    if name == 'exit':
        break
    elif name == 'voldemort':
        continue
    print(name)

print('The loop has completed')
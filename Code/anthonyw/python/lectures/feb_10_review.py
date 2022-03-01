

from datetime import timedelta
import random
# animals = ['bird', 'dog', 'cat', 'llama', 'panda', 'platypus']

# for animal in animals:
#     print(animal)

# animals[2] = 'lizard'

# for i in range(len(animals)):
#     print(animals[i])

# for i, animal in enumerate(animals):
#     print(i, animal)


# grades = {
#     'A': '90-100',
#     'B': '80-89',
#     'C': '70-79',
#     'D': '60-69',
#     'F': '0-59'
# }

# for key in grades:
#     print(key)

# for value in grades.values():
#     print(value)

# for key, value in grades.items():
#     print(key, value)

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# sorted_grades = {k: v for k, v in sorted(
#     grades.items(), key=lambda item: item[1])}
# print(sorted_grades)


# numbers = [1, 2, 3, 4]
# numbers[0] = 14
# numbers = tuple(numbers)
# numbers = list(numbers)
# numbers[-1] = 16
# numbers = tuple(numbers)
# print(numbers)

# def greet(name):
#     greeting = f"Hello {name}!"

#     return greeting, name


# output, name = greet("Dan")
# print(name)

# x = "b"
# y = "a"

# x, y = y, x

# print(x)
# print(y)

# pet = ("apple", "banana")
# pet = 4


# def get_letter_grade(grade):
#     letter = ''
#     if grade >= 90:
#         letter = 'A'
#     elif grade >= 80:
#         letter = 'B'
#     elif grade >= 70:
#         letter = 'C'
#     elif grade >= 60:
#         letter = 'D'
#     else:
#         letter = 'F'
#     return letter


# users_grade = int(input("Enter your grade: "))
# gary_grade = random.randint(1, 99)
# user_letter = get_letter_grade(users_grade)
# gary_letter = get_letter_grade(gary_grade)


# def print_banner(message):
#     border = "-" * len(message)
#     print(border)
#     print(message)
#     print(border)


# print_banner("Hello World!")


# numbers = [12, 14, 16, 18]
# sum = 0
# for num in numbers:
#     sum += num


# print(sum)


# animals = ['bird', 'dog', 'cat', 'llama', 'panda', 'platypus', "lizard"]


# cat_dog = animals[2:4:1]  # [start : end : count]

# print(cat_dog)
# import sample_module

# print("----------------")
# print("This is the review file")
# print(f"My __name__ is {__name__}")


import time
start = time.time()

# x = 0
# for i in range(100000):
#     x = i

# x = 0
# while x < 100000:
#     x += 1


end = time.time()
print(start, end)
print(end - start)

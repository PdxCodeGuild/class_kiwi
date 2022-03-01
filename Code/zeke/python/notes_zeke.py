# import random
# import string

# class Jackalope:
#     #Initialize jacklope with an age
#     def __init__ (self, name, sex, age =0, pregnant = False):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.pregnant = pregnant 
#     #increase age by 1
#     def aging(self):
#         self.age += 1
#     def get_pregnant(self, left, right):
#         if self.sex == 'f':
#             if self.age <= self.age<= 8:
#                 if left.sex == 'm' and 4 <= left.age <= 8:
#                     self.pregnant = True
#                 elif right.sex == 'm and 4 <= right.age <= 8:
#         else:
#             return

#     #Define how to print a 
#     def __str__(self):
#         return str(self.age)
#     #compare age between 2 jackalopes
#     def __gt__(self, jackalope):
#         return self.age >jackalope.age

# def generate_name():
#     name = ''
#     vowels = 'aeiouy'
#     not_vowels = 'bcdfghjklmnpqrstvwxz'
#     for i in range(4):
#         name += random.choice(string. ascii_lowercase)
#         name += random.choice(vowels)
#     return name

# def generate_sex():
#     sex = 'mf'
#     sex == random.choice(sex)


# herd = [] # Empty list of jackalopes
# # add two jackalopes to our herd list
# herd.append(Jackalope(0))
# herd.append(Jackalope(generate_name(), 'f')

# year = 0
# while len(herd) < 1000:
#     year += 1
#     print(f'Year: {year}. Population: {len(herd)}')
#     #check to see if jackalopes can mate
#     for index, jackalope in enumerate(herd):
#         #increase age of all jackalopes by 1
#         jackalope.aging()

#         if jackalope.pregnant:
#             herd.append
#         for jackalope in herd:
#             jackalope.aging()

#             if 4 <= jackalope.age <=8:
#                 herd.append(Jackalope(0))
#                 herd.append(Jackalope(0))
#             elif jackalope.age>= 10:
#                 herd.remove(jackalope)

###################################################



'''
#anatomy of a funcation
def funcation_name(parameters):
    """docstring"""
    statement1
    statement2
    ...
    ...
    return_what do you want to get out of the funcation_-some  expression
'''
import random

def top_five(first_name, last_name,):
    '''
    Print a welcome message to the console_ Docstring get exactly what the funcation should do.
    '''
    # print(f'Hello {first_name} {last_name}')

top_five("Micheal", "Jordan")
top_five("Stephen", "Curry")
top_five("Derrick", "Rose")
top_five("Kevin", "Durrant")
top_five("Klay", "Thompson")


top_five_count = 0
top_five_list = []
top_five = [
"Micheal Jordan"
"Stephen Curry"
"Derrick Rose"
"Kevin Durrant"
"Klay Thompson"
]

for i in range(len(top_five)):
    top_five=random.randint(1,5)
    top_five_list.append(top_five_list)
    print(top_five_list)



"""
Mob Programming: Jackalope Simulator

The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.

Gestation is instantaneous. Each gestation produces two offspring.

Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

With these conditions in mind, we can represent our population as a list of classes.
"""


import random
import string

class Jackalope:
    # initialize jackalope with an age
    def __init__(self, name, sex, age=0, pregnant=False):
        self.name = name
        self.sex =sex
        self.age = age
        self.pregnant = pregnant

    # increase age by one
    def aging(self):
        self.age += 1
    
    def get_pregnant(self, left, right):
        if self.sex == 'female' and self.pregnant == False:
            if 4 <= self.age <= 8:
                if left.sex == 'male' and 4 <= left.age <= 8:
                    self.pregnant = True
                elif right.sex == 'male' and 4 <= right.age <= 8:
                    self.pregnant = True
        else:
            return

    # define how to print jakalopes age
    def __str__(self):
        return str(self.age) # or f'{self.age}'
    # compare age betwen jackalopes
    def __gt__(self, jackalope):
        return self.age > jackalope.age

def gen_name():
    name = ''
    vowels = 'aeiouy'
    not_vowls = 'bcdfghjklmnpqrstvwxz'
    for i in range(2):
        name += random.choice(not_vowls)
        name += random.choice(vowels)

def generate_sex():
    sex = ['male', 'female']
    return random.choice(sex)

population = [] # or [Jackalope(0),Jackalope(0)]

# adding two jackalops to polulation
population.append(Jackalope('jack','male'))
population.append(Jackalope('jill','female'))


print(len(population))
year = 0
while len(population) < 1000:
    print(f'The current population is {len(population)} and the current year is {year}')
    if len(population) == 0:
        break
    year += 1

    #shuffle population
    

    # check to see if jackalopes can mate
    for i, jack in enumerate(population):

        # incrase jackalopes age
        jack.aging()
        
        if jack.pregnant == True:
            population.append(Jackalope(gen_name(),generate_sex()))
            population.append(Jackalope(gen_name(),generate_sex()))
            jack.pregnant = False
        
        left_jack = population[i - 1]

        if jack == population[-1]:
            right_jack = population[0]
        else:
            right_jack = population[i + 1]
        jack.get_pregnant( left_jack, right_jack)

        if jack.age >= 10:
            population.remove(jack)
    random.shuffle(population)

print(f'it took {year} years to make {len(population)}')

"""

# print(population) # [<__main__.Jackalope object at 0x000001E0E3EA7D60>, <__main__.Jackalope object at 0x000001E0E400BB20>]
# for thing in population:
#     print(thing)
#     # 0
#     # 0

# Version 1
year = 0
while len(population) < 1000:
    year += 1
    # print(len(population))
    # check to see if jackalopes can mate
    for jack in population:
        # incrase jackalopes age
        Jackalope.aging(jack)
        if 4 <= jack.age <= 8:
            population.append(Jackalope(0))
            population.append(Jackalope(0))
        elif jack.age >= 10:
            population.remove(jack)
    
# print(max(population))

"""







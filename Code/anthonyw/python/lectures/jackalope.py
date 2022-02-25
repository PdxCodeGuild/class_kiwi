"""
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of classes.
"""

"""
Now let's give the jackalopes distinct sexes and extend their gestation period to one year. 
We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. 
A jackalope will have the following properties:

name
age
sex
whether they're pregnant
Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.
"""




import random
import string
class Jackalope:

    # Initialize jackalope with an age
    def __init__(self, name, sex, age=0, pregnant=False):
        self.name = name
        self.age = age
        self.sex = sex
        self.pregnant = pregnant

    # Increase age by 1
    def aging(self):
        self.age += 1

    def get_pregnant(self, left, right):
        if self.sex == 'f' and self.pregnant == False:
            if 4 <= self.age <= 8:
                if left.sex == 'm' and 4 <= left.age <= 8:
                    self.pregnant = True
                elif right.sex == 'm' and 4 <= right.age <= 8:
                    self.pregnant = True

    # Define how to print a jackalope
    def __str__(self):
        return str(self.age)

    # Compare age between 2 jackalopes
    def __gt__(self, jackalope):
        return self.age > jackalope.age


def generate_name():
    name = ''
    vowels = 'aeiouy'
    not_vowels = "bcdfghjklmnpqrstvwxz"
    for i in range(2):
        name += random.choice(not_vowels)
        name += random.choice(vowels)

    return name


def generate_sex():
    sex = "mf"
    sex = random.choice(sex)
    return sex


herd = []  # Empty list of jackalopes
# Add two jackalopes to our herd list
herd.append(Jackalope(generate_name(), 'm'))
herd.append(Jackalope(generate_name(), 'f'))

year = 0
while len(herd) < 1000:
    if len(herd) == 0:
        break
    random.shuffle(herd)
    year += 1
    print(f"Year: {year}. Population: {len(herd)}")

    # Check to see if any jackalopes can mate
    for index, jackalope in enumerate(herd):
        # Increase age of all jackalopes by 1
        jackalope.aging()

        if jackalope.pregnant:
            herd.append(Jackalope(generate_name(), generate_sex()))
            herd.append(Jackalope(generate_name(), generate_sex()))
            jackalope.pregnant = False

        left_jackalope = herd[index - 1]
        if jackalope == herd[-1]:
            right_jackalope = herd[0]
        else:
            right_jackalope = herd[index + 1]
        jackalope.get_pregnant(left_jackalope, right_jackalope)

        if jackalope.age >= 10:
            herd.remove(jackalope)

print(f"It took {year} years to reach {len(herd)} jackalopes")

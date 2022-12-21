# Version 1
# The goal is to calculate how many years it will take for two jackalopes
#  to create a population of 1000.

# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.
import random
import string 

class Jackolope:
    #Initialize jackolope with an age 
    def __init__(self, name, sex, age=0, pregnant = False):
        self.name = name 
        self.age = age
        self.sex = sex
        self.pregnant = pregnant 
    # Increase age by 1
    def aging(self):
        self.aging +=1

    def get_pregnant (self, left, right):
        if self.sex == "f" and self.pregnant == False:
            if 4 <= self.age <= 8:
                if left.sex == "m" and 4 <= self.age <= 8:
                    self.pregnant = True 
                elif right.sex == "m" and 4 <= self.age <= 8:
                    self.pregnant = True 

        else:
            return 

    # Define how to print a jackolope 
    def __str__(self):
        return str(self.age)
    
    def generate_name():
        name = ''
        vowels = 'aeiouy'
        for i in range(2):
            name += random.choice (string.ascii_lowercase)
            name += random.choice (vowels)
        return name 

    def generate_sex():
        sex = "mf"
        sex = random.choice(sex)
        return sex

herd = [] # Empty list of jackolopes 
# Add two jackalopes to our herd list 
herd.append(Jackolope(generate_name(), 'm')
herd.append(Jackolope(generate_name(), 'f')
random.shuffle(herd)

year = 0
while len(herd) < 1000:
    year += 1
    # check to see if any jackolopes can mate 
    for index, jackolope in enumerate (herd):
    # Increase age of all jackalopes by 1    
        jackolope.aging()

        if jackolope.pregnant:
            herd.append(Jackolope(0))
            herd.append(Jackolope(0))

        left_jackolope = herd[index -1]
        right_jackolope = herd[herd +1]
        jackolope.get_pregnant(left_jackolope, right_jackolope)

        if jackolope.age <= 10:
            herd.remove(jackolope)

print (f'It took {year} years to reach {len(herd)} jackolopes.')
print(max(herd))

    
# for animal in herd:
#     print(animal)

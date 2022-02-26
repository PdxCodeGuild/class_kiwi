# Version 1
# The goal is to calculate how many years it will take for two jackalopes
#  to create a population of 1000.

# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.

class Jackolope:
    #Initialize jackolope with an age 
    def __init__(self, age):
        self.age = age 
    # Increase age by 1
    def aging(self):
        self.aging +=1
    # Define how to print a jackolope 
    def __str__(self):
        return str(self.age)
        
herd = [] # Empty list of jackolopes 
# Add two jackalopes to our herd list 
herd.append(Jackolope(0))
herd.append(Jackolope(0))

year = 0
while len(herd) < 1000:
    year += 1
    # check to see if any jackolopes can mate 
    for jackolope in herd:
    # Increase age of all jackalopes by 1    
        jackolope.aging()

        if 4<= jackolope.age <= 8:
            herd.append(Jackolope(0))
            herd.append(Jackolope(0))
        elif jackolope.age > 10:
            herd.remove(jackolope)
print (f'It took {year} years to reach {len(herd)} jackolopes.')


    
# for animal in herd:
#     print(animal)

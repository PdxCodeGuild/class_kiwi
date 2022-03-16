# Version 1

# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

# With these conditions in mind, we can represent our population as a list of ints.

def jackalope(end_pop):
    population = []
    years = 0
    for i in range(end_pop):
        for rabbit in population: # one gestation a year? Technically if the gestation is instantaneous then at age 4, the parents could have 498 gestations one right after the other within milliseconds
            rabbit += 1 # add a year to each rabbit for each loop
            if rabbit in population >= 4 and rabbit in population <=8:
                x = 1
                population.append(x)
            elif index, rabbit in enumerate(population) == 10:
                population.pop(index)
            elif len(population) == end_pop:
                break



    return 



    







# Version 2

# Now let's give the jackalopes distinct sexes and extend their gestation period to one year.
#  We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries.
# A jackalope will have the following properties:
#     name
#     age
#     sex
#     whether they're pregnant

# Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.

def jackalopeV2(end_pop):
    import random
    d = ["M", "F"]
    sex = random.choice(d)
    # list of generic names
    with open("names.txt", 'r') as file:
        names = file.read()
        name = names.split()
  




    population = []
    years = 0
    for i in range(end_pop):
        for rabbit in population: # one gestation a year? Technically if the gestation is instantaneous then at age 4, the parents could have 498 gestations one right after the other within milliseconds
            rabbit += 1 # add a year of age for every loop
            if rabbit in population[{"Sex"}] == "F" and rabbit in population[{"Age"}]>=4 and rabbit in population[{"Age"}] <=8:
                population.append({"Pregnant?": "Yes"})
            elif rabbit in population >= 4 and rabbit in population <=8:
                x = 1
                population.append({"Name" : name, "Age" : x, "Sex" : sex, "Pregnant?": "No"})
            elif index, rabbit in enumerate(population) == 10:
                population.pop(index)
            elif len(population) == end_pop:
                break



    return 


jackalopeV2(100)
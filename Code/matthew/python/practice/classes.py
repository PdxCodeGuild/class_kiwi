"""

# define a new class type
class Animal:
    # Class atributes
    legs = 4 
    species = "dog"
    color = "brown"
    fur = True

wiggles = Animal()

spot = Animal()
spot.color = 'black'

# print(type(wiggles)) #  <class '__main__.Animal'>

# print(wiggles.species) # dog
# print(wiggles.fur) # True
# print(spot.color) # black
"""







class Animal():

    # __init__(self) = initialize self, refering to the inilitalization of its self
    def __init__(self,name,legs,species,color,fur):  
        self.name = name
        self.legs = legs
        self.species = species
        self.color = color
        self.fur = fur

    def __str__(self,): # __str__(self) = allows you to print class a str
        return f"{self.name} is a {self.species} and has {self.legs} legs and is the color {self.color}. {'Has fur' if self.fur else 'No fur'}"

    def say_hi(self, sound): # using external information
        return f"{self.name} says {sound}"

    def run(self):
        if self.legs > 0:
            return f"{self.name} can run"
        else:
            return f"{self.name} can not run"



snek = Animal('snek', 0,'snake', 'red and orange', False)
spot = Animal('spot', 4, 'dog', 'brown', True)


# print(snek.legs) # 0
# print(spot.legs) # 4
# print(snek.say_hi("Sss")) # snek says Sss
# print(spot.run()) # spot can run


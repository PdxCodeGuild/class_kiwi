
# class Animal:  # Class definition
#     # Defined attributes on this class
#     legs = 4
#     species = "dog"
#     color = "brown"
#     fur = True


# wiggles = Animal()
# spot = Animal()
# spot.color = 'black'

# sneaky = Animal()
# sneaky.legs = 0
# sneaky.species = 'snake'
# sneaky.color = 'red and orange'
# sneaky.fur = False

# print(sneaky.color)


class Animal:
    def __init__(self, name, legs, species, color, fur):
        self.name = name
        self.legs = legs
        self.species = species
        self.color = color
        self.fur = fur

    def __str__(self):
        return f"{self.name} is a {self.species} and has {self.legs} legs, is the color {self.color}. {'Has fur' if self.fur else 'No fur'}"

    def say_hi(self, sound):
        return f"{self.name} says {sound}"

    def run(self):
        if self.legs > 0:
            return f"Watch {self.name} go!"
        else:
            return f"{self.name} didn't do much..."


sneaky = Animal('sneaky', 0, 'snake', 'red and orange', False)
spot = Animal('spot', 3, 'dog', 'white', True)

print(sneaky.run())

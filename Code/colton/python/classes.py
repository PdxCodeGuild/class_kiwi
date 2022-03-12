class Mushroom:
    def __init__(self, genus, species, location):
        self.genus = genus
        self.species = species
        self.location = location
    def __str__(self):
        return f"Genus:{self.genus} Species:{self.species} Location:{self.location}"

    def isa_psyc(self, psychadelic):
        if self == "No":
            return f"{self.genus}{self.species} is {psychadelic}"
        else:
            return f"{self}{psychadelic}"




user_input = input("Enter genus")
user_input2 = input("Enter species")
user_input3 = input("Enter location")

amanita_m = Mushroom(user_input, user_input2, user_input3)
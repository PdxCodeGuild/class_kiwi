'''         +-+#^#+--+#^#+--+#^#+-+             
             Project: Contact List                ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/18/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''
import json
# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values')
#  together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. 
# Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. 
# The text in the header represents the keys, the text in the other lines represent the values.
"""Created contacts.csv file with names"""
# with open("names.txt", "r")as file:
#     names = file.read()

# name = names.split()


# with open("contacts.csv", "w") as file:
#     file.write(f"{name}")
    
"""Created Colors.csv file"""
# with open("colors.csv") as file:
#     colors = file.read()

# color = colors.split("\n")

# while("" in color):
#     color.remove("")

# with open("colors.csv", "r") as file:
#     colors = file.read()

# color = colors.split(",")


with open("colors.json", "r") as file:
    colors = json.loads(file.read())





# import random
# colors = list(colors)
# random_color = random.choice(colors)

# print(colors)









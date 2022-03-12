# with open('words.txt', 'r') as file:
#     file_contents = file.read()

# print(file_contents)


# # 'r' - read - default
# # 'w' - write - overwrites
# # 'a' - append


# with open('words.txt', 'w') as file:
#     file.write('Johnson')


# with open('words.txt', 'a') as file:
#     file.write('\n Johnson')

# if '-- no edit' not in file_contents:
#     with open('words.txt', 'a') as file:
#         file.write('\n Johnson')


# with open("scoreboard.csv") as file:
#     contents = file.read()
#                     # .readlines()


# contents = contents.split('\n')

# # [{'name' : 'brad', 'score' : 3}]
scoreboard = []
# headers = contents[:1]
# players = contents[1:]

# for i, player in enumerate(players):
#     player = player.split(',')
#     scoreboard.append({'name': player[0], 'score': player[1]})



import json

with open('scoreboard.json', 'w') as file:
    file.write(json.dumps(scoreboard))

with open('scoreboard.json') as file:
    player_scores = json.loads(file.read())


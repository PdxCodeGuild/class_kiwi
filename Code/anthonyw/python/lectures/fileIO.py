
# with open('example.txt') as file:
#     file_contents = file.read()

# print(file_contents)

# with open modes
# 'r' - read -- default
# 'w' - write
# 'a' - append

# with open('example.txt', 'a') as file:
#     file.write('\nTGIF')

# with open("dictionaries.py") as py_file:
#     contents = py_file.read()

# print(contents)

import json
# with open("scoreboard.csv") as file:
#     contents = file.read()

# contents = contents.split('\n')
# print(contents)

# [{'name': 'brad', 'score': 3}]
# scoreboard = []
# headers = contents[:1]
# players = contents[1:]

# for index, player in enumerate(players):
#     player = player.split(',')
#     scoreboard.append({'name': player[0], 'score': player[1]})

# with open('scoreboard.csv', 'w') as file:
#     file.write(f'{scoreboard}')

# with open('scoreboard.json', 'w') as file:
#     file.write(json.dumps(scoreboard))

# with open('scoreboard.json') as file:
#     player_scores = json.loads(file.read())

# print(type(player_scores))

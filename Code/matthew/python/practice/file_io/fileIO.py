'''
with open('example.txt', 'r') as file:
     file_contents = file.read()

# print(file_contents)

# default 'r' - read
# 'w' - write
# 'a' - append
# 'rb' - read binary
# 'wb' - write binary

if '-- no edit' not in file_contents:
    with open('example.txt', 'a') as file:
        file.write('\nNew words')

with open('example.txt', 'a') as file:
    file.write('\nNew words')
'''

# with open('score.fakefiletype') as file:
#     contents = file.read()
# print(contents)

# with open('score.csv') as file:
#     contents = file.readlines()
# print(contents)

with open('score.csv') as file:
    contents = file.read()

contents = contents.split()
# print(contents) # ['name,', 'score', 'brad,3', 'susan,4', 'dan,12']

scoreboard = []

headline = contents[:1]

players = contents[1:]

# print(players,headline)

for index, player in enumerate(players):
    player = player.split(',')
    # print(player)
    scoreboard.append({'name': player[0], 'score':player[1]})

# print(scoreboard) # [{'name': 'brad', 'score': '3'}, {'name': 'susan', 'score': '4'}, {'name': 'dan', 'score': '12'}]


import json

with open('scoreboard.json', 'w') as file:
    file.write(json.dumps(scoreboard))

with open('scoreboard.json') as file:
    player_scores = json.loads(file.read())

# print(player_scores) # [{'name': 'brad', 'score': '3'}, {'name': 'susan', 'score': '4'}, {'name': 'dan', 'score': '12'}]


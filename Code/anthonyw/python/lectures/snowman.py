import random

with open('words.txt') as file:
	words = file.read().split()

secret_word = random.choice(words)
display_word = list("_" * len(secret_word))

print(secret_word)
print(" ".join(display_word))

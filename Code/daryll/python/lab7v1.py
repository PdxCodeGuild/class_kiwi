alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z", " "]
rot13_list = ["n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", " "]

word_convert = list(input("Enter a word to convert: ").lower())
rot13_convert = []
rot13_word = []
# Iterates through user inputted word (word_convert) and returns the index of the letter in alpha_list and adds it to rot13_convert list
for letter in word_convert:
    rot13_convert.append(alpha_list.index(letter))
# Iterates through rot13_convert index list and returns the letter in the rot13_list and adds it to rot13_word list
for letter in rot13_convert:
    rot13_word.append(rot13_list[letter])
print(f"Rot 13 Conversion: {''.join(rot13_word)}")
    
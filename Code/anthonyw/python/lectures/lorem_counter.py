
# create a list that will be our dictionary of words
with open('words.txt') as word_file:
    words = word_file.read()

dictionary = words.split('\n')


# convert loremipsum.txt into individual words
with open('loremipsum.txt') as lorem_file:
    lorem = lorem_file.read()

# remove periods from string
lorem = lorem.replace('.', '')
# remove comas from string
lorem = lorem.replace(',', '')
# split on all whitespace
lorem_words = lorem.split()

# remove duplicates from lorem_words
no_dups = list(set(lorem_words))


counter = 0
# check each word against our dictionary for match
for word in no_dups:
    if word in dictionary:
        # if there is a match +1 to our counter
        counter += 1

# print the counter in the terminal
print(f"We found {counter} words in the dictionary")

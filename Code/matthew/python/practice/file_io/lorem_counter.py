

# create a list that will be our dictionary of words
with open("words.txt") as file:
    words = file.read()

words = words.split('\n')

# convert loremipsum.txt into indidual words
with open("loremipsum.txt") as lorem_file:
    lorem_words = lorem_file.read()
# remove periods
lorem_words = lorem_words.replace(',', '')
# remove comas
lorem_words = lorem_words.replace('.', '')
# split on all whitesplace  (turns the string into list) 
lorem_words = lorem_words.split()

# print(lorem_words)

# remove duplicates from lorem_words
no_duplicates = list(set(lorem_words))


# check each word against our dictionary
counter = 0
for word in no_duplicates:
    if word in words:
        # if there is a match +1 to counter
        counter += 1 
print(counter)



# print the counter





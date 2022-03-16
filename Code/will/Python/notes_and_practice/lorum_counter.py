

with open('words.txt') as file:
    word_list = file.read()

dictionary = word_list.split('\n')
#print(dictionary)

with open('lorumipsum.txt') as lorem:
    ipsum = lorem.read()

# remove commas from string
ipsum = ipsum.replace(',', '')
# remove periods from string
ipsum = ipsum.replace('.', '')
# split on all whitespace
ipsum_list = ipsum.split()
#print(ipsum_list)

# remove dupes
no_dupes = list(set(ipsum_list))


common_words = 0

for word in no_dupes:
    if word in dictionary:
        common_words += 1


print(f'We found {common_words} common words.')
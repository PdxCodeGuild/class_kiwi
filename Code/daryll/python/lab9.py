ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}
characters = 0
words = 0
sentences = 0

with open("the_time_machine.txt", encoding = "utf-8") as ttm:
    ttm_contents = ttm.read()
# print(ttm_contents)

# split ttm_contents into characters
for character in ttm_contents:
    if character == "." or character == ",":
        character = ""
    characters += 1
# print(characters)

# split contents into words
ttm_split_contents = ttm_contents.replace(".", "")
ttm_split_contents = ttm_contents.replace(",", "")
ttm_split_contents = ttm_contents.split()
words = len(ttm_split_contents)
# print(words)

# split ttm_contents into sentences
ttm_sentences = ttm_contents.split(".")
sentences = len(ttm_sentences)
# print(sentences)

ari_index = round(4.71 * (characters / words) + (0.5 * (words / sentences)) - 21.43)
# print(ari_index)

for key in ari_scale:
    if key == ari_index:
        output = ari_scale[key]
print(f"\nThe ARI for {ttm.name} is {ari_index}")
print(f"This corresponds to a {ari_scale[ari_index]['grade_level']} Grade level of difficulty")
print(f"that is suitable for an average person {ari_scale[ari_index]['ages']} years old")
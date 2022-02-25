'''         +-+#^#+--+#^#+--+#^#+-+             
  Project: Compute Automated Readability Index    ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 2/16/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''


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

def compute_ari(text):
    """Gives applicable reading level for designated text"""
    #4.71(chars/words) + 0.5(words/setences) - 21.43 rounding up to full number#
    
    title = ''

    # Get number of characters
    chars = len(text.replace(' ', ''))

    # Get number of words
    words = len(text.split())
    
    # Get number of sentences
    sentences = int(text.count('.') + text.count('?') + text.count('!'))
  
    # Get ARI level
    x = round((chars/words)* 4.71 + (words/sentences)* 0.5 - 21.43)
    if x > 14:
        x == 14

    output = f"""
    --------------------------------------------------------------------
    The ARI for {title} is {x}
    This corresponds to a {ari_scale[x]['grade_level']} level of difficulty
    That is suitable for an average person {ari_scale[x]['ages']} years old.
    --------------------------------------------------------------------
    """

    # Return ARI level with text
    return output


def main():

    with open('War_and_Peace.txt', encoding="utf8") as text:
        text = text.read()

    print(compute_ari(text))



if __name__ == "__main__":
    main()


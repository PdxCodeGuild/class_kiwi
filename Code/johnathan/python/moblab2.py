
# # Snowman

# Let's write a program to play a game of [Snowman](https://en.wikipedia.org/wiki/Snowman_(game))! Snowman is a word game where a secret word is chosen, then players have to guess letters until they get the word correct or they run out of chances and lose.


# ## Part 1

# ## Loading the Words

# Using `with open()` let's load a list of words from a file. This will be used to select our secret word.
# ## Part 1

# Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, 
# show the blanks with the letters filled in. If they guess a letter which is not in the word, 
# tell them and subtract 1 from their remaining guesses. Allow the user 10 tries to guess the letters of the word. 
# If the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

# Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.import random
# ```python
from dataclasses import replace
import random
from timeit import repeat

# def blanks_function():
#     blanks_list = []
#     for blank in range(blanks):
#         blanks_list.append('_')

#     blanks_list = ",".join(blanks_list)  

#     blanks_list = blanks_list.replace(",", " ")
#     return blanks_list

def str_converter(x):
    x = "".join(x)
    return x


# blanks = len(random_word) 
snowman_pics = [r'''

 (   ) 
''', r'''


 (   )
 (   ) 
''', r'''

 (   )
 (   )
 (   ) 
''', r'''

 (   )
 (   )
 ( : )
''', r'''

 (   )
 ( : )
 ( : )
''', r'''

 ( . )
 ( : )
 ( : )
''', r'''
 _===_ 
 ( . )
 ( : )
 ( : )
''', r'''
 _===_ 
 ( .O)
 ( : )
 ( : )
''',r'''
 _===_ 
 (-.O)
 ( : )
 ( : )
''', r'''
 _===_ 
 (-.O) 
<( : )
 ( : ) 
''', r'''
 _===_ 
 (-.O) 
<( : )\
 ( : ) 
''']

with open('snowman.txt', 'r') as file:
    text = file.read()
text = text.split('\n')
word = len(text)

play_again = True

while play_again == True:

    random_word = random.choice(text)
    print (random_word)

    blanks = len(random_word) 
    blanks_list = []
    for blank in range(blanks):
        blanks_list.append('_')

    blanks_list = ",".join(blanks_list)  

    blanks_list = blanks_list.replace(",", "")
    print(blanks_list)
    guess_count = 9
    
    guess_list = []
    while '_' in blanks_list and guess_count > 1:
        snow_num = 10 - guess_count
        user_guess = input('Please guess a letter: ')
        
        if user_guess in guess_list:
            print(f'You already guessed {user_guess}. Please, make a different selection.')
            
        elif guess_count == 0:
            break
        elif user_guess not in random_word:
            guess_count -= 1
            print(f'Your {user_guess} is not correct. Please, guess again.')
            print(snowman_pics[snow_num])
        elif len(user_guess) > 2:
            if user_guess == random_word:
                print(f'Congrats! You guessed {random_word}.')
                break
            else:
                print(f'Incorrect guess. Try again.')
                guess_count -= 1
                print(snowman_pics[snow_num])
        letters_found = 0 
        for x, y in enumerate(random_word):
            if y == user_guess:
                letters_found += 1
                blanks_list = list(blanks_list)
                blanks_list[x] = user_guess
                # print (x,y)
        guess_list.append(user_guess)
        print(f'Guesses remaining: {guess_count}')
        print(f'{letters_found} {user_guess} were found.')
        print(str_converter(blanks_list))
    repeat = input("Do you want to play again; select: y or n: ")
    if repeat == 'n':
        print('Thanks for playing!')
        play_again = False


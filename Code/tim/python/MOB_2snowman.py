## Timothy Hampton, Zeke Wells, Victory, Joseph Brown-Womack, Eric Hollister
##Snowman
import random
## Open word.txt
with open('words.txt', 'r') as file:
    text = file.read()
# print(text)

## Use random function to pick secret word
word_list = text.split('\n')

play = True
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

while play == True:
    secret_word = random.choice(word_list)
    
    ## Figure out how many characters are in the word to show blanks
    char_length = len(secret_word)
    # print(char_length)

    ## Generate blanks = to char_length
    blanks = ''
    for char in secret_word:
        blanks += '_ '
    print(blanks)

    ## guesses
    guesses = -1
    guesses_r = 10
    guessed_list = []
    ## creating 10 guesses
    ## figure out the index for the letter guessed and the same blank
    while guesses < 10:
        
        letter = input('Guess a letter ').lower()
        if not letter.isalpha():
            print('Not a letter. Guess again.')
            continue
        
        if len(letter) > 1:
            if letter == secret_word:
                print(f'You win!! The word was {secret_word}')
                break
            
            else:
                print(f'You lose :( The secret word was {secret_word}')
                print(snowman_pics[10])
                break
        
        if letter in guessed_list:
            print(f'You have already guessed {letter}!')
            continue
        else:
            guessed_list
        
        if letter in secret_word:
            secret_list = list(secret_word)
            blanks_list = blanks.split(' ')
            
            for i in range(len(secret_list)):
                if letter == secret_list[i]:
                    blanks_list[i] = letter
                    
            blanks = " ".join(blanks_list)
            print(f'{letter} found \n{blanks} \nGuesses remaining: {guesses_r}')
            
        else:
            guesses += 1
            guesses_r -= 1
            print(f'{letter} not found. Guesses remaining {guesses_r}')
            print(snowman_pics[guesses])
            if guesses == 10:
                print(f'Game over. Too many guesses. The word was: {secret_word}')

    answer = input('Do you want to play again (y/n): ').lower()
    if answer == 'n':
        play = False

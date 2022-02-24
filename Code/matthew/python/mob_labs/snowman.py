"""
Let's write a program to play a game of Snowman! Snowman is a word game where a secret word is chosen, 
then players have to guess letters until they get the word correct or they run out of chances and lose.
"""
def snowman():
    import random

    def make_blanks(blanks):
        blank_list = []
        for blank in range(blanks):
            blank_list.append('_')
        blank_list =",".join(blank_list)
        blank_list = blank_list.replace(',','')
        return blank_list

    def str_converter(x):
        x = "".join(x)
        # x = x.replace(',','')
        return x

    with open("snowmanwords.txt") as file:
        snowman = file.read()

    snowman = snowman.split()
    word = len(snowman)
    random_word = random.choice(snowman)
    blanks = len(random_word)
    blank_str = make_blanks(blanks)

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
    
    # print(random_word)
    # while True:
    guess_count = 9
    guess_list = []
    while '_' in blank_str:
        
        if guess_count == 0:
            break
        user_guess = input('Please guess a letter: ')
          
        if user_guess in guess_list:
            print(f'\nYou have already guessed {user_guess}')
        
        if len(user_guess) > 2:
            if user_guess == random_word:
                print(f'You guessed the random word {random_word}!')
                break
            else:
                guess_count -= 1
                print(f'Your guess of {user_guess} was incorrect')
                print(f'You have {guess_count} guesses remaning')
        elif user_guess not in random_word:
            guess_count -= 1
            print(f'\n{user_guess} is not in the word')
            print(f'You have {guess_count} guesses remaning')
            print(snowman_pics[10-user_guess])
            print(str_converter(blank_str))
        else:
            letters_found = 0
            for i, value in enumerate(random_word):

                if value == user_guess:
                    letters_found += 1
                    blank_str = list(blank_str)
                    blank_str[i] = user_guess
                    # print(i, 'i')
                    # print(value,"value")
            blank_str = str_converter(blank_str)
            print(f'\n{letters_found} {user_guess} was found')
            print(blank_str)
        guess_list.append(user_guess)
            

if __name__ == '__main__':
    play_again = 'y'
    while play_again.lower() == 'y':
        snowman()
        play_again = input("Would you like to play again? (y/n) ")
        if play_again == 'n':
            break
        # elif play_again != 'y' or 'n':
        #     print(f'{play_again} is not a valid option')


    
    


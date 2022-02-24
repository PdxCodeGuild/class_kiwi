# # MOB LAB: Colton, Daryll, Lis, Renan, Anthony, Gage

import random
#     # Import text file 

with open("words.txt") as file:
     text = file.read()


# # VERSION 1


# # Generate random word from text
# # def random_word_gen(text):

# # Split text into a list
# text = text.split()
# random_word = list(random.choice(text))
    
# random_word_copy = random_word.copy()

# print(random_word_copy)
# # return random_word


# # Display amount of spaces in the word
# spaces = len(random_word_copy) * '_'.split(',')

# # Loop the input until done (Guessing the letters 10 times)
# counter = 10
# correct_guess = []
# user_guess = []
# while counter > 1:
#     # Grab input from the user
#     user_input = input('Guess a letter: ')
#     user_guess.append(user_input)
#     # Sub 1 for each wrong guess
#     if user_input not in random_word_copy:
#         counter -= 1
#         print(f"Incorrect guess! you have {counter} guesses left.")
#     # Show the correct positioned guesses on the dotted line
#     elif user_input in random_word_copy:
        
#         letter_index = random_word_copy.index(user_input) # The index of each correct letter
#         spaces[letter_index] = user_input # Changes the correct space to letter
#         if spaces == random_word_copy:
#             print(f"Congrats!{spaces} was the correct word.")
#             break
        
#         print(f'{letter_index} - letter index')
#         print(spaces)
    
# # Check if they already guessed a letter





# # VERSION 2

# # Split text into a list
# text = text.split()
# random_word = list(random.choice(text))
    
# random_word_copy = random_word.copy()

# print(random_word_copy)
# # return random_word


# # Display amount of spaces in the word
# spaces = len(random_word_copy) * '_'.split(',')

# # Loop the input until done (Guessing the letters 10 times)
# counter = 10
# incorrect_guess = [] # Stores every incorrect guess
# correct_guess = [] #  Stores every correct guess
# while counter > 1:
#     # Grab input from the user
#     print(spaces)
#     user_input = input('Guess a letter: ')
#     if user_input in incorrect_guess + correct_guess:
#         print("You already guessed that")
#         continue
#     # Sub 1 for each wrong guess
#     if user_input not in random_word_copy:
#         counter -= 1
#         print(f"Incorrect guess! you have {counter} guesses left.")
#         incorrect_guess.append(user_input)
#         print(f"{incorrect_guess} Were the wrong letters.")
#     # Show the correct positioned guesses on the dotted line
#     elif user_input in random_word_copy:
        
#         letter_index = random_word_copy.index(user_input) # The index of each correct letter
#         spaces[letter_index] = user_input # Changes the correct space to letter
#         correct_guess.append(user_input)
#         print(f"{correct_guess} Were the correct letters.")
#         if spaces == random_word_copy:
#             print(f"Congrats!{spaces} was the correct word.")
#             break
    




# # VERSION 3

# # Split text into a list
# text = text.split()
# random_word = list(random.choice(text))
    
# random_word_copy = random_word.copy()

# print(random_word_copy)
# # return random_word


# # Display amount of spaces in the word
# spaces = len(random_word_copy) * '_'.split(',')

# # Loop the input until done (Guessing the letters 10 times)
# counter = 10
# incorrect_guess = [] # Stores every incorrect guess
# correct_guess = [] #  Stores every correct guess
# while counter > 1:
#     # Grab input from the user
#     print(spaces)
#     user_input = input('Guess a letter: ')
#     # Checks if user input whole word correctly
#     if list(user_input) == random_word_copy:
#         print( f"Congrats! {random_word_copy} was the correct word.")
#         break
#     elif user_input in incorrect_guess + correct_guess:
#         print("You already guessed that")
#         continue
#     # Sub 1 for each wrong guess
#     elif user_input not in random_word_copy:
#         counter -= 1
#         print(f"Incorrect guess! you have {counter} guesses left.")
#         incorrect_guess.append(user_input)
#         print(f"{incorrect_guess} Were the wrong letters.")
#     # Show the correct positioned guesses on the dotted line
#     elif user_input in random_word_copy:
        
#         letter_index = random_word_copy.index(user_input) # The index of each correct letter
#         spaces[letter_index] = user_input # Changes the correct space to letter
#         correct_guess.append(user_input)
#         print(f"{correct_guess} Were the correct letters.")
#         if spaces == random_word_copy:
#             print(f"Congrats!{spaces} was the correct word.")
#             break
    
# # Allow the user to user to guess the whole word



# VERSION 4
# # snowman_pics = ['''



# #  (   ) 
# # ''', '''


# #  (   )
# #  (   ) 
# # ''', '''

# #  (   )
# #  (   )
# #  (   ) 
# # ''', '''

# #  (   )
# #  (   )
# #  ( : )
# # ''', '''

# #  (   )
# #  ( : )
# #  ( : )
# # ''', '''

# #  ( . )
# #  ( : )
# #  ( : )
# # ''', '''
# #  _===_ 
# #  ( . )
# #  ( : )
# #  ( : )
# # ''', '''
# #  _===_ 
# #  ( .O)
# #  ( : )
# #  ( : )
# # ''','''
# #  _===_ 
# #  (-.O)
# #  ( : )
# #  ( : )
# # ''', '''
# #  _===_ 
# #  (-.O) 
# # <( : )
# #  ( : ) 
# # ''', '''
# #  _===_ 
# #  (-.O) 
# # <( : )>
# #  ( : ) 
# # ''']
# # # Split text into a list
# # text = text.split()
# # random_word = list(random.choice(text))
    
# # random_word_copy = random_word.copy()

# # # return random_word


# # # Display amount of spaces in the word
# # spaces = len(random_word_copy) * '_'.split(',')

# # # Loop the input until done (Guessing the letters 10 times)
# # counter = -1
# # guess_counter = 10
# # incorrect_guess = [] # Stores every incorrect guess
# # correct_guess = [] #  Stores every correct guess
# # while counter < 10:
# #     # Grab input from the user
# #     print(spaces)
# #     user_input = input('Guess a letter: ')
# #     # Checks if user input whole word correctly
# #     if list(user_input) == random_word_copy:
# #         print( f"Congrats! {random_word_copy} was the correct word.")
# #         break
# #     elif user_input in incorrect_guess + correct_guess:
# #         print("You already guessed that")
# #         continue
    
# #     # Sub 1 for each wrong guess
# #     elif user_input not in random_word_copy:
# #         counter += 1
# #         guess_counter -= 1
# #         print(f"Incorrect guess! you have {guess_counter} guesses left.")
# #         incorrect_guess.append(user_input)
# #         print(f"{incorrect_guess} Were the wrong letters.")
# #         print(snowman_pics[counter])
# #         if guess_counter == -1:
# #             print( f"You've ran out of guess's. The correct word was {random_word_copy}")
# #     # Show the correct positioned guesses on the dotted line
# #     elif user_input in random_word_copy:
        
# #         letter_index = random_word_copy.index(user_input) # The index of each correct letter
# #         spaces[letter_index] = user_input # Changes the correct space to letter
# #         correct_guess.append(user_input)
# #         print(f"{correct_guess} Were the correct letters.")
# #         if spaces == random_word_copy:
# #             print(f"Congrats!{spaces} was the correct word.")
# #             break
    


# snowman_pics = ['''



#  (   ) 
# ''', '''


#  (   )
#  (   ) 
# ''', '''

#  (   )
#  (   )
#  (   ) 
# ''', '''

#  (   )
#  (   )
#  ( : )
# ''', '''

#  (   )
#  ( : )
#  ( : )
# ''', '''

#  ( . )
#  ( : )
#  ( : )
# ''', '''
#  _===_ 
#  ( . )
#  ( : )
#  ( : )
# ''', '''
#  _===_ 
#  ( .O)
#  ( : )
#  ( : )
# ''','''
#  _===_ 
#  (-.O)
#  ( : )
#  ( : )
# ''', '''
#  _===_ 
#  (-.O) 
# <( : )
#  ( : ) 
# ''', '''
#  _===_ 
#  (-.O) 
# <( : )>
#  ( : ) 
# ''']




# # IN PROGRESS - managing double letter words

# # # Split text into a list
# # text = text.split()
# # random_word = list(random.choice(text))
# # loop = True
# # while loop == True:
# #     random_word = list(random.choice(text))
# #     random_word.sort()
# #     print(random_word)
# #     for index in range(len(random_word)):
# #         if random_word[index] == random_word[index + 1]:
# #             loop == True
# #         else:
# #             loop == False
# #     break
# # random_word_copy = random_word.copy()

# # # return random_word


# # # Display amount of spaces in the word
# # spaces = len(random_word_copy) * '_'.split(',')
# # print(random_word_copy)
# # # Loop the input until done (Guessing the letters 10 times)
# # counter = -1
# # guess_counter = 10
# # incorrect_guess = [] # Stores every incorrect guess
# # correct_guess = [] #  Stores every correct guess
# # while counter < 10:
# # # Grab input from the user
# #     print(spaces)
# #     user_input = input('Guess a letter: ')


            


# #     # Checks if user input whole word correctly
# #     if list(user_input) == random_word_copy:
# #         print( f"Congrats! {random_word_copy} was the correct word.")
# #         break
# #     elif user_input in incorrect_guess + correct_guess:
# #         print("You already guessed that")
# #         continue

# #     # Sub 1 for each wrong guess
# #     elif user_input not in random_word_copy:
# #         counter += 1
# #         guess_counter -= 1
# #         print(f"Incorrect guess! you have {guess_counter} guesses left.")
# #         incorrect_guess.append(user_input)
# #         print(f"{incorrect_guess} Were the wrong letters.")
# #         print(snowman_pics[counter])
# #         if guess_counter == -1:
# #             print( f"You've ran out of guess's. The correct word was {random_word_copy}")
# #     # Show the correct positioned guesses on the dotted line
# #     elif user_input in random_word_copy:
        
# #         letter_index = random_word_copy.index(user_input) # The index of each correct letter
# #         spaces[letter_index] = user_input # Changes the correct space to letter
# #         correct_guess.append(user_input)
# #         print(f"{correct_guess} Were the correct letters.")
# #         if spaces == random_word_copy:
# #             print(f"Congrats!{spaces} was the correct word.")
# #             break
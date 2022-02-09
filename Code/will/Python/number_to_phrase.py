# Number to Phrase - Version 1

# tens = {1: 'ten',
# 2: 'twenty ',
# 3: 'thirty ',
# 4: 'forty ',
# 5: 'fifty ',
# 6: 'sixty ',
# 7: 'seventy ',
# 8: 'eighty ',
# 9: 'ninety '
# }
# ones = {1: 'one',
# 2: 'two',
# 3: 'three',
# 4: 'four',
# 5: 'five',
# 6: 'six',
# 7: 'seven',
# 8: 'eight',
# 9: 'nine'
# }

# def number_to_phrase(number):

#     tens_place = number // 10
#     ones_place = number % 10

#     tens_phrase = tens.get(tens_place)

#     if tens_place not in tens.keys():
#         tens_phrase = ''

#     ones_place = number % 10

#     ones_phrase = ones.get(ones_place)

#     if ones_place not in ones.keys():
#         ones_phrase = ''

#     while True:
#         if tens_place == 1 and ones_place == 1:
#             number_phrase = 'eleven'
#             break
#         elif tens_place == 1 and ones_place == 2:
#             number_phrase = 'twelve'
#             break
#         elif tens_place == 1 and ones_place == 3:
#             number_phrase = 'thirteen'
#             break
#         elif tens_place == 1 and ones_place == 4:
#             number_phrase = 'fourteen'
#             break
#         elif tens_place == 1 and ones_place == 5:
#             number_phrase = 'fifteen'
#             break
#         elif tens_place == 1 and ones_place == 6:
#             number_phrase = 'sixteen'
#             break
#         elif tens_place == 1 and ones_place == 7:
#             number_phrase = 'seventeen'
#             break
#         elif tens_place == 1 and ones_place == 8:
#             number_phrase = 'eighteen'
#             break
#         elif tens_place == 1 and ones_place == 9:
#             number_phrase = 'nineteen'
#             break
#         else:
#             number_phrase = f'{tens_phrase}{ones_phrase}'
#             break

#     return number_phrase

# def main():
#     number = int(input('Please enter a number: '))

#     phrase = number_to_phrase(number)

#     print(phrase)

    
# main()



# Number to Phrase - Version 2

hundreds = {1: 'one hundred ',                                                                                                                                                      # dictionaries to hold all phrase info
2: 'two hundred ',
3: 'three hundred ',
4: 'four hundred ',
5: 'five hundred ',
6: 'six hundred ',
7: 'seven hundred ',
8: 'eight hundred ',
9: 'nine hundred '
}

tens = {1: 'ten',
2: 'twenty ',
3: 'thirty ',
4: 'forty ',
5: 'fifty ',
6: 'sixty ',
7: 'seventy ',
8: 'eighty ',
9: 'ninety '
}
ones = {1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine'
}

def number_to_phrase(number):     
        
    '''function used to convert number value into string phrase equivalent'''                                           

    hundreds_place = number // 100                                                                                                                                                  # math to determine hundreds place
    hundreds_phrase = hundreds.get(hundreds_place)

    if hundreds_place not in hundreds.keys():
        hundreds_phrase = ''

    tens_place = (number - hundreds_place * 100) // 10                                                                                                                              # math to determine tens place
    tens_phrase = tens.get(tens_place)

    if tens_place not in tens.keys():
        tens_phrase = ''

    ones_place = (number - hundreds_place * 100) % 10                                                                                                                               # math to determine ones place
    ones_phrase = ones.get(ones_place)

    if ones_place not in ones.keys():
        ones_phrase = ''

    while True:                                                                                                                                                                     # loop to define 11 - 19 to simplify dictionaries

        if tens_place == 1 and ones_place == 1:
            number_phrase = f'{hundreds_phrase}eleven'
            break

        elif tens_place == 1 and ones_place == 2:
            number_phrase = f'{hundreds_phrase}twelve'
            break

        elif tens_place == 1 and ones_place == 3:
            number_phrase = f'{hundreds_phrase}thirteen'
            break

        elif tens_place == 1 and ones_place == 4:
            number_phrase = f'{hundreds_phrase}fourteen'
            break

        elif tens_place == 1 and ones_place == 5:
            number_phrase = f'{hundreds_phrase}fifteen'
            break

        elif tens_place == 1 and ones_place == 6:
            number_phrase = f'{hundreds_phrase}sixteen'
            break

        elif tens_place == 1 and ones_place == 7:
            number_phrase = f'{hundreds_phrase}seventeen'
            break

        elif tens_place == 1 and ones_place == 8:
            number_phrase = f'{hundreds_phrase}eighteen'
            break

        elif tens_place == 1 and ones_place == 9:
            number_phrase = f'{hundreds_phrase}nineteen'
            break

        else:
            number_phrase = f'{hundreds_phrase}{tens_phrase}{ones_phrase}'
            break

    return number_phrase                                                                                                                                                            # return phrase to main function

def main():
    
    while True:                                                                                                                                                                     # try/except loop to ensure valid value is entered

        try:                                                                                                                                                                        
            number = int(input('Please enter a number: '))  

        except ValueError:
            print('Letters and symbols are not excepted.')

        else:
            phrase = number_to_phrase(number)
            print(phrase)
            break
    
main()




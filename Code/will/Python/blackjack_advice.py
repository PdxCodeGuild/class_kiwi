#Blackjack Advice - Version 1

# card_values = {'A': 1,
# '2': 2,
# '3': 3,
# '4': 4,
# '5': 5,
# '6': 6,
# '7': 7,
# '8': 8,
# '9': 9,
# '10': 10,
# 'J': 10,
# 'Q': 10,
# 'K': 10
# }




# def advice_calculator(card_one, card_two, card_three):

#     card_one_value = card_values.get(card_one)
#     card_two_value = card_values.get(card_two)
#     card_three_value = card_values.get(card_three)

#     if card_one_value + card_two_value + card_three_value < 17:
#         return 'Hit.'

#     elif card_one_value + card_two_value + card_three_value >= 17 and card_one_value + card_two_value + card_three_value < 21:
#         return 'Stay.'
    
#     elif card_one_value + card_two_value + card_three_value == 21:
#         return 'Blackjack!'

#     else:
#         return 'Already Busted.'


# def main():

#     print('Want some blackjack advice? Please enter any face card as the first letter of the card.')

#     card_one = input('What is your first card? ' )
#     card_one = card_one.upper()

#     card_two = input('What is your second card? ')
#     card_two = card_two.upper()

#     card_three = input('What is your third card? ')
#     card_three = card_three.upper()

#     advice = advice_calculator(card_one, card_two, card_three)

#     print(f'{advice}')

# main()




# Blackjack Advice - Version 2

card_values = {'A': 11,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10
}

def advice_calculator(card_one, card_two, card_three):

    card_one_value = card_values.get(card_one)
    card_two_value = card_values.get(card_two)
    card_three_value = card_values.get(card_three)
    total = card_one_value + card_two_value + card_three_value

    while True:

        if total < 17:
            return 'Hit.'

        elif total >= 17 and total < 21:
            return 'Stay.'
    
        elif total == 21:
            return 'Blackjack!'

        elif total > 21 and card_one == 'A':
            card_one_value = 1

            if total > 21 and card_two == 'A':
                card_two_value = 1

                if total > 21 and card_three == 'A':
                    card_three_value = 1

        elif total > 21 and card_two == 'A':
            card_two_value = 1

            if total > 21 and card_three == 'A':
                card_three_value = 1

        elif total > 21 and card_three == 'A':
            card_three_value = 1
        else:
            return 'Already Busted.'


def main():

    print('Want some blackjack advice? Please enter any face card as the first letter of the card.')

    card_one = input('What is your first card? ' )
    card_one = card_one.upper()

    card_two = input('What is your second card? ')
    card_two = card_two.upper()

    card_three = input('What is your third card? ')
    card_three = card_three.upper()

    advice = advice_calculator(card_one, card_two, card_three)

    print(f'{advice}')

main()
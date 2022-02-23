print('Welcome to Blackjack, I will advise you based on your card values \n')

#Assign Values for the cards
card_values = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

#Next create a list of the cards
#Get Values of list
#Condition if the list is....

first_card = input('Please enter the first card: ' ).upper()
second_card = input('Please enter the second card: ').upper()
third_card = input('Please enter the third card: ').upper()

tot_cardval = card_values[first_card] + card_values[second_card] + card_values[third_card]
print(f"The total values of your cards is {tot_cardval}. My advise for you is ")

#print(total_values)

def black_jack(tot_cardval):
    if tot_cardval < 17:
        return "Hit"
    elif 17 <= tot_cardval <= 20:
        return "Stay"
    elif tot_cardval == 21:
        return "Blackjack"
    elif tot_cardval >= 21:
        return "Already Busted"
    else:
        print('Wrong values, please try again')

print(black_jack(tot_cardval))




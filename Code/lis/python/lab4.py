# Lab 4

# create dictionary
card_values = {
  'A':1,
  '2':2,
  '3':3,
  '4':4,
  '5':5,
  '6':6,
  '7':7,
  '8':8,
  '9':9,
  '10':10,
  'J':10,
  'Q':10,
  'K':10
}

# create function
def blackjack(first_card, second_card, third_card): 

# get dictionary values and add together
  if all (key in card_values for key in (first_card, second_card, third_card) ):
    sum_value = (card_values.get(first_card) + card_values.get(second_card) + card_values.get(third_card))

    # determine classification of added values
    if sum_value < 17:
      return(f'{sum_value} Hit')
    elif 17 <= sum_value < 21:
      return(f'{sum_value} Stay')
    elif sum_value == 21:
      return(f'{sum_value} Blackjack!')
    elif sum_value > 21:
      return(f'{sum_value} Already Busted')
    else:
      return(f"Please enter a valid card value next time: {', '.join(card_values.keys())}")
      
# get inputs
print(f"Select a card: {', '.join(card_values.keys())}")

first_card = input("What's your first card? ").upper()
second_card = input("What's your second card? ").upper()
third_card = input("What's your third card? ").upper()

# call function
print(blackjack(first_card, second_card, third_card))
import random
cards = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k"]
card_1 = random.choice(cards)
card_2 = random.choice(cards)

print(f"\nYour cards are: {card_1}, and {card_2}")

if card_1 == "a":
    card_1 = 11
elif card_1 == "k" or card_1 == "q" or card_1 == "j":
    card_1 = 10
else:
    card_1 = int(card_1)

if card_1 == 11 and card_2 == "a":
    card_2 = 1
elif card_1 <= 10 and card_2 == "a":
    card_2 = 11
elif card_1 == 11 and card_2 == "k" or card_2 == "q" or card_2 == "j":
    card_2 = 10
elif card_1 <= 10 and card_2 == "k" or card_2 == "q" or card_2 == "j":
    card_2 = 10
else:
    card_2 = int(card_2)

card = 0
total = card_1 + card_2 + card

def advice(total):
    if total == 21:
        return f"{total} Blackjack!!\n"
    elif total > 21:
        return f"{total} Already Busted!\n"
    elif total < 17:
        return f"{total} hit"
    elif total >= 17:
        return f"{total} stay\n"
print(advice(total))

while advice(total) == f"{total} hit":
    answer = input("\nDo you want another card (yes, no)? ")
    if answer == "no":
        print("\n")
        break
    elif answer == "yes":
        card = random.choice(cards)
        print(f"Your card is: {card}")
        if total <= 10 and card == "a":
            card = 11
        elif total >= 11 and card == "a":
            card = 1
        elif card == "k" or card == "q" or card == "j":
            card = 10
        else:
            card = int(card)
        total += card
    print(f"{advice(total)}")

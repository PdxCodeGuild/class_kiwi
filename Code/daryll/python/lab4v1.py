card_count = 1
total = 0
while card_count < 4:
    card = input(f"What is your card {card_count}? ")
    if card == "k" or card == "q" or card == "j":
        card = 10
    elif card == "a":
        card = 1
    card_count += 1
    total += int(card)

def advice(total):
    if total == 21:
        return f"{total} Blackjack!!"
    elif total > 21:
        return f"{total} Already Busted!"
    elif total < 17:
        return f"{total} hit"
    elif total >= 17:
        return f"{total} stay"

print(advice(total))
# Lab 05 - Pick 6 - Versions 1 and 2 - Working

#imports
import random

#generate 6 random unique numbers between 1 and 99, .sample will not allow duplicates
def gen_nums():
    nums = random.sample(range(1, 99), 6)
    return nums

#zip two lists together, return the sum of identical item/element pairs (or matches)
def match(a, b):
    match = sum(x == y for x, y in zip(a, b))
    return match

#assign the winning numbers
wnums = gen_nums()

#player purchases x tickets
def pick(x):
    i = 0
    #define a list for matches, 0-6, set each to 0 
    m = [0, 0, 0, 0, 0, 0, 0]
    #define balance and set to zero
    b = 0
    #simulate purchasing and checking x player tickets against winning numbers
    while i < x:
        #deduct 2 from balace
        b -= 2
        #generate player picks
        pnums = gen_nums()
        #add one to the list for matches element that corresponds with the number of matches
        m[match(wnums, pnums)] += 1
        i += 1
    #after loop completes, calculate earnings, expenses, balance and roi and display
    earnings = (m[1]*4 + m[2]*7 + m[3]*100 + m[4]*50000 + m[5]*1000000 + m[6]*25000000)
    expenses = abs(b)
    balance = b + earnings
    roi = (earnings - expenses) / expenses
    print(f'Your balance is ${balance:.2f}')
    print(f'Your expenses were ${expenses:.2f}')
    print(f'Your earnings were ${earnings:.2f}')
    print(f'Your ROI is {roi:.2%}')
pick(100000)

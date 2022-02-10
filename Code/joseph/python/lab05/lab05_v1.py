#Lab 05 - Pick 6 - Version 1 - In Progess

#imports
import lab05

#define empty lists for winning numbers
wnum = []
pnum = []

#define empty list for matches
m = []

#define function to pull winning numbers
def wnums():
    wnum.append(lab05.generate_numbers())
    return wnum

#define function to pull player numbers
def pnums():
    pnum.
    return pnum

#define function to compare player numbers to winning numbers
def match():
    m.append(sum(w == p for w, p in zip(wnum, pnum)))
    return m

#define function to combine the player pulls and match functions
def check(x):
    i=0
    while i < x:
        print(pnums(), match())
        i += 1
    print('done')



print(check(10))
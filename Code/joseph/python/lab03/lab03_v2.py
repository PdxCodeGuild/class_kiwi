# Lab 03 - Numbers to Phrase - Version 2 - 0-999 - Working

#Define Dictionary for the ones digit, zero through nineteen, since there is no tenty for 11-19
ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
    18: 'eighteen', 19: 'nineteen'
}

#Define dictionary for the tens digit, twenty through ninety
tens = {
    0: '', 1: '', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty',
    6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'
}

#Define dictionary for the hundreds digit, one hundred through nine hundred
hundo = {
    0: '', 1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred',
    5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred',
    9: 'nine hundred'
}

#Define function to convert integer to English
def numEng(n):
    '''Converts a number to its English phrase
    numEng(n: integer) -> string'''
    if n == 0:
        return 'ZipZilchNada'
    if n < 20:
        return ones[n]
    if n < 100:
        return str(tens[n//10] + ' ' + ones[n % 10])
    if n < 1000:
        #return str(hundo[n//100] + ' ' + tens[n//10] + ' ' + ones[n % 10]) <--First attempt failed
        #return hundo[n//100] works
        #return tens[n//10] <--Fails, need to remove hundreds from n before running tens math
        h = n//100 #to get hundreds digit and store it as h
        t = n - h*100 #to get tens digit, subtract h*100 from n
        o = t % 10 #to get ones digit
        return str(hundo[h] + ' ' + tens[t//10] + ' ' + ones[o])


print(numEng(645))
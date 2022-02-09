# Lab 03 - Numbers to Phrase - Version 1 - 0-99 - Working

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


print(numEng(23))
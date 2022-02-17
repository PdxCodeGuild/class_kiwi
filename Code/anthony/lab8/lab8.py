###  Lab 8    ###
################################
##                            ##
##   Lab 8: Peaks and Valleys ##
##   Author: Anthony Bilie    ##
##   Date: 2/16/2022          ##
##                            ##
################################
# Version 1
# Define the following functions:

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

# make list for data and index
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 8, 8, 9]

# peak function


def peak(data):
    peaks = []
    for x in range(len(data)-1):
        if data[x-1] < data[x] > data[x+1]:
            peaks.append(x)
    return peaks
# valleys function


def valleys(data):
    valleys = []
    for x in range(1, len(data)):
        if data[x-1] > data[x] < data[x+1]:
            valleys.append(x)
    return valleys
# peaks and valleys function


def peaks_and_valleys(data):
    high = peak(data)
    low = valleys(data)
    total = sorted(high + low)
    return total


print(peaks_and_valleys(data))

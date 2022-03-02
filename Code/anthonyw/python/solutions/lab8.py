"""
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the 
        left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and 
        valleys in order of appearance in the original data.
"""

# define test data
#                         p        v              p        v
import random
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#       0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
# peaks function to return indices of peaks


def peaks():
    peak_indices = []
    # loop over data
    for i in range(1, len(data) - 1):
        # compare current index with previous and next values
        next = data[i + 1]
        previous = data[i - 1]
        current = data[i]
        # if previous and next are both lower value than current, we found a peak
        if previous < current > next:
            peak_indices.append(i)

    return peak_indices


# valleys function to return indices of valleys
def valleys():
    valley_indices = []
    # loop over data
    for i in range(1, len(data) - 1):
        # compare current index with previous and next values
        # if previous and next are both higher value than current, we found a valley
        if data[i - 1] > data[i] < data[i + 1]:
            valley_indices.append(i)

    return valley_indices


# peaks_and_valleys function to return indices of both peaks and valleys in order of appearance
def peaks_and_valleys():
    p_indices = peaks()
    v_indices = valleys()

    peaks_valleys = p_indices + v_indices

    peaks_valleys.sort()
    return peaks_valleys


def print_peaks_and_valleys():
    rows = max(data)
    cols = len(data)
    for i in range(rows, 0, -1):
        for j in range(cols):
            if i > data[j]:
                print('  ', end=" ")
            else:
                print(' X', end=" ")

        print()

    print(data)


def print_peaks_and_valleys_with_water():
    # data.reverse()
    rows = max(data)
    cols = len(data)
    peaks_valleys = peaks_and_valleys()
    for row in range(rows, 0, -1):
        for col in range(cols):
            cell = ' '
            for i in range(len(peaks_valleys) - 1):
                previous = peaks_valleys[i]
                next = peaks_valleys[i + 1]
                if row <= data[col]:
                    cell += 'X'
                    break
                elif previous < col <= next:
                    cell += 'O'
                    break
                elif row > data[col]:
                    cell += ' '
                    break
            print(cell, end=" ")

        print()

    print(data)


print_peaks_and_valleys_with_water()
# data = []
# for i in range(20):
#     data.append(random.randint(1, 9))


# print_peaks_and_valleys()
# print(peaks_and_valleys())

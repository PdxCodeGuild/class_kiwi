# Lab 8: Version 1
'''
Define the following functions:
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. 
A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys 
in order of appearance in the original data.

Visualization of test data:
Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V			
'''

# list containing data
data = [1, 2, 3, 4, 5, 6, 7, 6,	5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8,	9]

# peak function iterating through data list and comparing values on either side of index
def peaks():
    peaks = []
    for index, value in enumerate(data):
        if index != 0 and index != 20:
            if data[index - 1] < value > data[index + 1]:
                peaks.append(index)
    
    return peaks

print(peaks())

# valley function iterating through data list and comparing values on either side of index
def valleys():
    valleys = []
    for index, value in enumerate(data):
        if index != 0 and index != 20:
            if data[index - 1] > value < data[index + 1]:
                valleys.append(index)
    
    return valleys

print(valleys())

# peaks_and_valleys function combining two functions and sorting to appear in order
def peaks_and_valleys():
    peaks_and_valleys = sorted(peaks() + valleys())

    return peaks_and_valleys

print(peaks_and_valleys())

# peaks_and_valleys function to return indices of both peaks and valleys in order of appearance

def peaks_and_valleys_graphics():
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

print(peaks_and_valleys_graphics())


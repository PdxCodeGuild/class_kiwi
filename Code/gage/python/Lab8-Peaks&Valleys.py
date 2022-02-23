
'''

VERSION 1

# Data: 23456765456789876789
base_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
#                           P           V              P        V

# Stores index values of the peaks
def peaks(data):

    # Storage for final peak values
    peaks = []
    
    # Collects the index and item value for each number
    for index, item in enumerate(data[0:-1]):
        if item > data[index - 1] and item > data[index + 1]: # If the item is greater then the previous and next number after it, it will append
            peaks.append(index)
    return peaks


def valleys(data):
    
    # Storage for final valley values
    valleys = []

    # Collects the index and item value for each number
    for index, item in enumerate(data):
        if item < data[index - 1] and item < data[index + 1]: # If the item is less then the previous and next number after it, it will append
                valleys.append(index)
               
        if len(valleys) >= 3: # Removes values that aren't known to be a peak or valley
                valleys.pop(0)
    return valleys


def p_v(peak_i, valley_i):
    # Collects and adds the lists together from the peaks and valleys
    peaks_valleys = peak_i + valley_i
    peaks_valleys.sort() # Sorts and orders the list
    return peaks_valleys


print( f"""
The peaks are {peaks(base_data)}
The valleys are {valleys(base_data)}
The correct order for these peaks and valleys is {p_v(peaks(base_data), valleys(base_data))}
""")


'''

# VERSION 2 NOT CORRECT - not sure how to display a 90 degree image
# X 
# X X 
# X X X
# X X X X
# X X X X X
# X X X X X X
# X X X X X X X
# X X X X X X
# X X X X X
# X X X X
# X X X X X
# X X X X X X
# X X X X X X X
# X X X X X X X X
# X X X X X X X X X
# X X X X X X X X
# X X X X X X X
# X X X X X X
# X X X X X X X
# X X X X X X X X
# X X X X X X X X X

'''
VERSION 2

base_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

for index, item in enumerate(base_data):
    print("X " * item)

'''

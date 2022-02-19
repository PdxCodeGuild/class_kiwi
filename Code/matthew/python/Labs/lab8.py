"""
Lab 8: Peaks and Valleys
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on 
both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and 
valleys in order of appearance in the original data.

Visualization of test data:
Data	1	2	3	4	5	6	7	6	5	4	5	6	7	8	9	8	7	6	7	8	9
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20
POI							P			V					P			V			

"""

def peaks(data):
    """
    Returns the indices of peaks. A peak has a lower number on both the left and the right.
    """
    peaks = [] 
    for num in range(1, (len(data) - 1)): # itterating through the list looking for peaks
        if data[num - 1] < data[num] > data[num + 1]:
            peaks.append(num)
    return peaks

def valleys(data):
    """
    Returns the indices of 'valleys'. A valley is a number with a higher number on 
both the left and the right
"""
    valleys = [] 
    for num in range(1, (len(data) - 1)): # itterating through the list looking for valleys
        if data[num - 1] > data[num] < data[num + 1]:
            valleys.append(num)
    return valleys

def peaks_and_valleys(data):
    """
    uses the above two functions to compile a single list of the peaks and 
valleys in order of appearance in the original data"""
    peaks_valleys = []
    for num in peaks(data): # adding peaks to a combined list
        peaks_valleys.append(num)
    for num in  valleys(data): # adding valleys to the combined list
        peaks_valleys.append(num)
    return sorted(peaks_valleys) # returning peaks and valleys in numerical order


if __name__ == '__main__':
    data = [1,2,3,4,5,6,7,6,5,4,5,6,7,8,9,8,7,6,7,8,9]
    print(peaks_and_valleys(data))
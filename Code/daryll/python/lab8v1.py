data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(data):
    peak = []
    for index, value in enumerate(data):
        if index == 0:
            left_val = data[index]
        else:
            left_val = data[index - 1]
        if index == 20:
            right_val = data[index]
        else:
            right_val = data[index + 1]
        if left_val < value > right_val:
            peak.append(index)
    return peak
       
def valleys(data):
    valley = []
    for index, value in enumerate(data):
        if index == 0:
            left_val = data[index]
        else:
            left_val = data[index - 1]
        if index == 20:
            right_val = data[index]
        else:
            right_val = data[index + 1]
        if left_val > value < right_val:
            valley.append(index)
    return valley

def peaks_and_valleys():
    peak_valley = peaks(data) + valleys(data)
    peak_valley.sort()
    return peak_valley         

print(peaks(data))
print(valleys(data))
print(peaks_and_valleys())